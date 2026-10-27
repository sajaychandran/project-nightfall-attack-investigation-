import pandas as pd
import streamlit as st
from app import data
from src.evidence_analysis import filter_events

events, _, _, _ = data()
st.title("Evidence Explorer")
st.caption("Record what the telemetry says before writing what you think it means.")
query = st.text_input("Search evidence")
c1, c2, c3 = st.columns(3)
category = c1.selectbox("Category", ["All"] + sorted({e["event_category"] for e in events}))
host = c2.selectbox("Host / identity", ["All"] + sorted({e["host_or_identity"] for e in events}))
confidence = c3.selectbox("Source confidence", ["All", "High", "Medium", "Low"])
shown = filter_events(events, query, category, host, confidence)
st.download_button("Download filtered CSV", pd.DataFrame(shown).to_csv(index=False), "nightfall-evidence.csv", "text/csv")
st.dataframe(pd.DataFrame(shown)[["evidence_id","timestamp","event_category","host_or_identity","confidence","event_description"]], use_container_width=True, hide_index=True)
if shown:
    selected = st.selectbox("Inspect record", [e["evidence_id"] for e in shown])
    event = next(e for e in shown if e["evidence_id"] == selected)
    st.json(event)
    st.text_area("Analyst observation (session only)", key=f"obs_{selected}", placeholder="Describe only what is directly observed.")
    st.text_area("Alternative explanations (session only)", key=f"alt_{selected}")
    st.text_area("Additional evidence needed (session only)", key=f"need_{selected}")

