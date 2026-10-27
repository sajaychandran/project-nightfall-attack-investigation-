from __future__ import annotations

import pandas as pd
import plotly.express as px


def timeline_figure(events: list[dict]) -> object:
    frame = pd.DataFrame(events)
    if frame.empty:
        return px.scatter(title="No evidence selected")
    frame["timestamp"] = pd.to_datetime(frame["timestamp"], utc=True)
    return px.scatter(frame, x="timestamp", y="event_category", color="confidence",
                      hover_data=["evidence_id", "event_description"], text="evidence_id",
                      title="Synthetic evidence timeline", height=440)

