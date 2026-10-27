from __future__ import annotations

from typing import Any


def filter_events(events: list[dict[str, Any]], query: str = "", category: str = "All",
                  host: str = "All", confidence: str = "All") -> list[dict[str, Any]]:
    text = query.strip().lower()
    return [
        event for event in events
        if (not text or text in " ".join(str(value) for value in event.values()).lower())
        and (category == "All" or event.get("event_category") == category)
        and (host == "All" or event.get("host_or_identity") == host)
        and (confidence == "All" or event.get("confidence") == confidence)
    ]


def event_summary(events: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "records": len(events),
        "categories": len({event.get("event_category") for event in events}),
        "high_confidence": sum(event.get("confidence") == "High" for event in events),
    }

