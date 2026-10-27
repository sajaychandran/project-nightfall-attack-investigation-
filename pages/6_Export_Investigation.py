import json
import streamlit as st
from app import data
from src.navigator_export import build_layer, validate_layer
from src.report_generator import generate_report

events, _, _, _ = data()
st.title("Export Investigation")
st.caption("Export preserves analyst rationale and status in Navigator-compatible comments.")
layer = build_layer(st.session_state.mappings)
validate_layer(layer)
st.download_button("Download ATT&CK Navigator JSON", json.dumps(layer, indent=2), "project-nightfall-layer.json", "application/json")
report = generate_report(events, st.session_state.mappings, st.session_state.worksheet, st.session_state.recommendations)
st.download_button("Download Markdown investigation report", report, "project-nightfall-report.md", "text/markdown")
st.subheader("Navigator preview")
st.json(layer)

