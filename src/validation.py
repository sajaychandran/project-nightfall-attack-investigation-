from __future__ import annotations

from typing import Any


def validate_events(events: list[dict[str, Any]]) -> list[str]:
    errors = []
    seen: set[str] = set()
    for event in events:
        evidence_id = event.get("evidence_id")
        if not evidence_id:
            errors.append("An event is missing evidence_id.")
        elif evidence_id in seen:
            errors.append(f"Duplicate evidence ID: {evidence_id}")
        seen.add(evidence_id)
        if not event.get("timestamp"):
            errors.append(f"{evidence_id or 'Unknown'} is missing timestamp.")
    return errors

