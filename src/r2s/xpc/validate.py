from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from xpc.paths import schemas_dir

_REQUIRED: dict[str, frozenset[str]] = {
    "hypothesis": frozenset({"id", "claim", "falsifier", "success_metric", "status"}),
    "protocol": frozenset({"id", "hypothesis_id", "steps", "environment"}),
    "result": frozenset({"id", "hypothesis_id", "protocol_id", "verdict", "recorded_at"}),
    "run": frozenset({"id", "hypothesis_id", "protocol_id", "status"}),
}


def load_registry() -> Registry:
    reg = Registry()
    for p in schemas_dir().glob("*.schema.json"):
        data = json.loads(p.read_text(encoding="utf-8"))
        resource = Resource.from_contents(data)
        reg = reg.with_resource(data["$id"], resource)
        reg = reg.with_resource(p.name, resource)
    return reg


def detect_kind(instance: dict[str, Any]) -> str | None:
    keys = frozenset(instance)
    best: str | None = None
    best_score = -1
    for kind, req in _REQUIRED.items():
        if req <= keys:
            score = len(req)
            if score > best_score:
                best, best_score = kind, score
    return best


def validate_instance(instance: dict[str, Any], kind: str | None = None) -> str:
    kind = kind or detect_kind(instance)
    if kind is None:
        raise ValueError("cannot detect artifact kind; pass --kind")
    if kind not in _REQUIRED:
        raise ValueError(f"unknown kind: {kind}")
    schema_path = schemas_dir() / f"{kind}.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema, registry=load_registry()).validate(instance)
    return kind


def validate_file(path: Path, kind: str | None = None) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected JSON object")
    return validate_instance(data, kind=kind)
