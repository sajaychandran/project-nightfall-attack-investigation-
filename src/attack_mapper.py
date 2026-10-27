from __future__ import annotations

from typing import Any

VALID_STATUSES = {"proposed", "supported", "rejected", "further_investigation"}
STATUS_TRANSITIONS = {
    "proposed": VALID_STATUSES,
    "supported": {"supported", "rejected", "further_investigation"},
    "rejected": {"rejected", "proposed", "further_investigation"},
    "further_investigation": {"further_investigation", "proposed", "supported", "rejected"},
}


def search_techniques(techniques: list[dict[str, Any]], query: str = "", tactic: str = "All") -> list[dict[str, Any]]:
    needle = query.lower().strip()
    return [
        item for item in techniques
        if (not needle or needle in item["technique_id"].lower() or needle in item["name"].lower())
        and (tactic == "All" or item["tactic"] == tactic)
    ]


def validate_technique(techniques: list[dict[str, Any]], technique_id: str) -> dict[str, Any]:
    for technique in techniques:
        if technique["technique_id"] == technique_id:
            return technique
    raise ValueError(f"Unsupported ATT&CK technique ID: {technique_id}")


def add_mapping(mappings: list[dict[str, Any]], mapping: dict[str, Any],
                techniques: list[dict[str, Any]]) -> dict[str, Any]:
    technique = validate_technique(techniques, mapping.get("technique_id", ""))
    evidence_ids = mapping.get("evidence_ids", [])
    if not evidence_ids or not mapping.get("rationale", "").strip():
        raise ValueError("A mapping needs supporting evidence IDs and a rationale.")
    status = mapping.get("status", "proposed")
    if status not in VALID_STATUSES:
        raise ValueError(f"Unsupported mapping status: {status}")
    record = {**mapping, "technique_name": technique["name"], "tactic": technique["tactic"]}
    mappings.append(record)
    return record


def update_status(mapping: dict[str, Any], status: str) -> dict[str, Any]:
    current = mapping.get("status", "proposed")
    if status not in VALID_STATUSES or status not in STATUS_TRANSITIONS.get(current, set()):
        raise ValueError(f"Invalid mapping status transition: {current} -> {status}")
    if status == "supported" and not mapping.get("rationale", "").strip():
        raise ValueError("Supported mappings require an analyst rationale.")
    mapping["status"] = status
    return mapping

