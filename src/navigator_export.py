from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

NAVIGATOR_VERSION = "4.9.1"


def build_layer(mappings: list[dict[str, Any]], name: str = "Project Nightfall Investigation") -> dict[str, Any]:
    techniques = []
    for mapping in mappings:
        status = mapping.get("status", "proposed")
        score = {"supported": 3, "proposed": 2, "further_investigation": 1, "rejected": 0}.get(status, 0)
        comment = (
            f"Status: {status}; Analyst confidence: {mapping.get('confidence', 'Unassessed')}. "
            f"Evidence: {', '.join(mapping.get('evidence_ids', []))}. "
            f"Rationale: {mapping.get('rationale', '')}. "
            f"Alternatives: {mapping.get('alternative_explanations', '')}. "
            f"Missing evidence: {mapping.get('missing_evidence', '')}"
        )
        techniques.append({
            "techniqueID": mapping["technique_id"], "score": score,
            "color": "#2ca02c" if status == "supported" else "#ffb000" if status != "rejected" else "#999999",
            "comment": comment, "enabled": True,
        })
    return {
        "name": name, "versions": {"attack": "15", "navigator": NAVIGATOR_VERSION},
        "domain": "enterprise-attack",
        "description": "Synthetic Project Nightfall candidate mappings. Displayed techniques are not a confirmed attack sequence.",
        "filters": {"platforms": ["Windows", "Office 365", "Identity Provider"]},
        "sorting": 3, "layout": {"layout": "side", "showName": True},
        "hideDisabled": False, "selectTechniquesAcrossTactics": True,
        "techniques": techniques, "gradient": {"colors": ["#ffffff", "#ffb000", "#d62728"], "minValue": 0, "maxValue": 3},
        "legendItems": [
            {"label": "Supported (analyst assessment)", "color": "#2ca02c", "score": 3},
            {"label": "Candidate / further investigation", "color": "#ffb000", "score": 1},
            {"label": "Proposed", "color": "#ffb000", "score": 2},
            {"label": "Rejected", "color": "#999999", "score": 0},
        ],
        "metadata": {"case": "Project Nightfall", "synthetic": True, "generated_at": datetime.now(timezone.utc).isoformat()},
    }


def validate_layer(layer: dict[str, Any]) -> None:
    if layer.get("domain") != "enterprise-attack" or layer.get("versions", {}).get("attack") != "15":
        raise ValueError("Navigator layer must declare Enterprise ATT&CK version 15.")
    if not isinstance(layer.get("techniques"), list):
        raise ValueError("Navigator layer techniques must be a list.")

