#!/usr/bin/env python3
"""Read-only bridge from RCK discovery records to existing Codex Reuptake events.

No rewriting canonical event history. Standard library only.
"""
import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
EVENTS = ROOT / "Reuptake/provenance/event-log.jsonl"

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def read_events(path=EVENTS):
    events = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(f"Invalid JSONL at line {line_number}: {error}") from error
        if not isinstance(event, dict) or not event.get("event_id"):
            raise ValueError(f"Missing event_id at line {line_number}")
        events.append(event)
    return events

def build_index(events):
    by_id = {}
    for event in events:
        key = event["event_id"]
        if key in by_id:
            raise ValueError(f"Duplicate event_id: {key}")
        by_id[key] = event
    return by_id

def references(event):
    result = set()
    for key in ("paths", "files", "datasets", "registry_updates", "dependencies", "parent_events"):
        value = event.get(key, [])
        if isinstance(value, list):
            result.update(v for v in value if isinstance(v, str))
    for key in ("packet", "study", "registry"):
        if isinstance(event.get(key), str):
            result.add(event[key])
    return sorted(result)

def snapshot():
    events = read_events()
    index = build_index(events)
    registry = read_json(HERE / "registry.json")["entries"]
    sources = read_json(HERE / "sources.json")["sources"]
    # The original Relay records have heterogeneous fields; preserve them as-is.
    # RCK constructs are linked only through explicit event IDs or matching source paths.
    result = []
    for construct in registry:
        declared = construct.get("relay_event_ids", [])
        found = [key for key in declared if key in index]
        missing = [key for key in declared if key not in index]
        result.append({"construct_id": construct["id"], "linked_events": found,
                       "unresolved_event_ids": missing, "link_status": "linked" if found else "unlinked"})
    return {"event_count": len(events), "unique_event_count": len(index),
            "source_count": len(sources), "construct_count": len(registry),
            "construct_links": result, "coverage_status": "unknown",
            "warning": "Unlinked does not mean absent; source universe is not fully indexed."}

def query(term):
    needle = term.casefold()
    matches = []
    for event in read_events():
        if needle in json.dumps(event, ensure_ascii=False).casefold():
            matches.append({"event_id": event["event_id"], "date": event.get("date"),
                            "status": event.get("status"), "summary": event.get("summary"),
                            "references": references(event)})
    return matches

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "search", "snapshot"])
    parser.add_argument("terms", nargs="*")
    args = parser.parse_args()
    if args.command == "check":
        state = snapshot()
        print(json.dumps({"status": "PASS", "events": state["event_count"],
                          "constructs": state["construct_count"],
                          "linked_constructs": sum(bool(x["linked_events"]) for x in state["construct_links"]),
                          "coverage": state["coverage_status"]}, indent=2))
    elif args.command == "snapshot":
        print(json.dumps(snapshot(), indent=2, ensure_ascii=False))
    else:
        if not args.terms:
            parser.error("search requires a query")
        print(json.dumps(query(" ".join(args.terms)), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
