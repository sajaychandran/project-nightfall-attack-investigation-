from __future__ import annotations

from typing import Any


def generate_report(events: list[dict[str, Any]], mappings: list[dict[str, Any]],
                    hypotheses: list[dict[str, Any]], recommendations: list[dict[str, Any]]) -> str:
    lines = [
        "# Project Nightfall Investigation Report", "",
        "> **SIMULATED TRAINING CASE:** This report contains synthetic evidence only.",
        "", "## Executive summary",
        f"Investigation scope includes {len(events)} synthetic evidence records and {len(mappings)} candidate ATT&CK mappings.",
        "No hypothesis is treated as a confirmed incident finding without corroborating evidence.", "",
        "## Incident scope", "Fictional Northstar organisation; UTC timeline; synthetic identity, endpoint, mail, document and network records.", "",
        "## Evidence timeline",
    ]
    for event in sorted(events, key=lambda item: item["timestamp"]):
        lines.append(f"- **{event['timestamp']} — {event['evidence_id']} ({event['event_category']})**: {event['event_description']}")
    lines += ["", "## Candidate ATT&CK mappings"]
    if mappings:
        for mapping in mappings:
            lines.append(f"- **{mapping['technique_id']} {mapping.get('technique_name', '')}** — {mapping.get('status', 'proposed')}; confidence {mapping.get('confidence', 'Unassessed')}; evidence {', '.join(mapping.get('evidence_ids', []))}. Rationale: {mapping.get('rationale', '')}")
    else:
        lines.append("- No mappings recorded.")
    lines += ["", "## Investigation questions and limitations"]
    for hypothesis in hypotheses:
        lines.append(f"- **{hypothesis['hypothesis_id']}** {hypothesis['question']} — {hypothesis.get('conclusion') or 'Unresolved'}; next action: {hypothesis.get('next_action', '')}")
    lines += ["", "## Defensive recommendations"]
    for item in recommendations:
        lines.append(f"- **{item.get('action', '')}** ({item.get('purpose', '')}): {item.get('limitations', '')}")
    if not recommendations:
        lines.append("- Document preventive, detective and response measures in the Defensive Recommendations page.")
    lines += ["", "## Data provenance", "ATT&CK Enterprise v15; local subset documented in `data/attack_techniques.json`; synthetic records authored for this workshop.", "", "## Suggested next investigative steps", "Validate sign-in context, retrieve full process ancestry and correlate document objects with DLP or cloud-sync manifests."]
    return "\n".join(lines) + "\n"

