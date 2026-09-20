from __future__ import annotations

import argparse
import json
import sys

from r2s.handoff import handoff
from r2s.io import load_board, load_card
from r2s.rank import rank
from r2s.score import score, should_kill


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="r2s", description="r2s reference runtime CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rank = sub.add_parser("rank", help="Rank cards on a board")
    p_rank.add_argument("board", help="Path to board JSON")

    p_score = sub.add_parser("score", help="Score a single card")
    p_score.add_argument("card", help="Path to card JSON")

    p_hand = sub.add_parser("handoff", help="Emit handoff JSON for a card")
    p_hand.add_argument("card", help="Path to card JSON")
    p_hand.add_argument("--draft", help="Optional draft JSON with handoff fields")

    args = parser.parse_args(argv)

    if args.cmd == "rank":
        board = load_board(args.board)
        ranked = rank(board)
        out = []
        for card in ranked:
            killed, reason = should_kill(card)
            item = {"id": card["id"], "score": score(card), "status": card["status"]}
            if killed:
                item["kill_reason"] = reason
            out.append(item)
        json.dump(out, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    if args.cmd == "score":
        card = load_card(args.card)
        killed, reason = should_kill(card)
        payload = {"id": card["id"], "score": score(card), "killed": killed, "kill_reason": reason}
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    if args.cmd == "handoff":
        card = load_card(args.card)
        draft = None
        if args.draft:
            draft = json.loads(open(args.draft, encoding="utf-8").read())
        packet = handoff(card, draft=draft)
        json.dump(packet, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
