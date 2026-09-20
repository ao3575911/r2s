from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from r2s.errors import ValidationError
from r2s.paths import SCHEMAS_DIR


@lru_cache(maxsize=1)
def _registry() -> Registry:
    registry: Registry = Registry()
    for path in sorted(SCHEMAS_DIR.glob("*.schema.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        resource = Resource.from_contents(data)
        registry = registry.with_resource(str(data["$id"]), resource)
        registry = registry.with_resource(path.name, resource)
    return registry


def validate_instance(instance: Mapping[str, Any], schema_filename: str) -> None:
    schema_file = SCHEMAS_DIR / schema_filename
    if not schema_file.is_file():
        raise ValidationError(f"missing schema: {schema_filename}")
    schema = json.loads(schema_file.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, registry=_registry())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        first = errors[0]
        path = "/".join(str(p) for p in first.path) or "(root)"
        raise ValidationError(f"{schema_filename} @ {path}: {first.message}")
