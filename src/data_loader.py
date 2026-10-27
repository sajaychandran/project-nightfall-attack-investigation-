from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent


class DataValidationError(ValueError):
    """Raised when a local exercise dataset is malformed."""


def _read_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise DataValidationError(f"Unable to read valid JSON from {path}: {exc}") from exc


def load_incident(path: str | Path | None = None) -> dict[str, Any]:
    result = _read_json(Path(path) if path else BASE_DIR / "data" / "incident_events.json")
    if not isinstance(result, dict) or not isinstance(result.get("events"), list):
        raise DataValidationError("Incident data must contain an events list.")
    required = {"evidence_id", "timestamp", "host_or_identity", "event_category", "event_description"}
    for event in result["events"]:
        if not isinstance(event, dict) or not required.issubset(event):
            raise DataValidationError(f"Event is missing required fields: {event!r}")
    return result


def load_techniques(path: str | Path | None = None) -> dict[str, Any]:
    result = _read_json(Path(path) if path else BASE_DIR / "data" / "attack_techniques.json")
    if not isinstance(result, dict) or result.get("metadata", {}).get("attack_version") != "v15":
        raise DataValidationError("Technique catalogue must explicitly target ATT&CK v15.")
    if not isinstance(result.get("techniques"), list):
        raise DataValidationError("Technique catalogue must contain a techniques list.")
    return result


def load_hypotheses(path: str | Path | None = None) -> list[dict[str, Any]]:
    result = _read_json(Path(path) if path else BASE_DIR / "data" / "investigation_hypotheses.json")
    if not isinstance(result, list) or not all(isinstance(item, dict) for item in result):
        raise DataValidationError("Hypotheses must be a JSON list of objects.")
    return result


def sorted_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(events, key=lambda event: event["timestamp"])

