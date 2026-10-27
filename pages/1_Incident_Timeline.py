import streamlit as st
from app import data
from src.timeline import timeline_figure

events, _, _, _ = data()
st.title("Incident Timeline")
st.caption("All timestamps are synthetic UTC records. Proximity is not proof of causation.")
categories = ["All"] + sorted({e["event_category"] for e in events})
category = st.selectbox("Filter category", categories)
shown = events if category == "All" else [e for e in events if e["event_category"] == category]
st.plotly_chart(timeline_figure(shown), use_container_width=True)
for event in shown:
    with st.expander(f"{event['timestamp']} · {event['evidence_id']} · {event['event_category']}"):
        st.write(event["event_description"])
        st.caption(f"Observed: {event['observed_behaviour']} | Limitations: {event['evidence_limitations']}")

