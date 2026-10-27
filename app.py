from __future__ import annotations

import streamlit as st

from src.attack_mapper import add_mapping
from src.data_loader import load_hypotheses, load_incident, load_techniques, sorted_events
from src.evidence_analysis import filter_events
from src.navigator_export import build_layer, validate_layer
from src.report_generator import generate_report
from src.timeline import timeline_figure

st.set_page_config(page_title="Project Nightfall", page_icon="🌙", layout="wide")
st.markdown("""<style>
.stApp { background: #f7f9fc; } .hero { padding: 1.4rem; border-radius: 12px; background: linear-gradient(120deg,#102a43,#1f5f8b); color:white; }
.warning { padding: .8rem 1rem; border-left: 5px solid #e09f3e; background:#fff8e7; }
</style>""", unsafe_allow_html=True)

@st.cache_data
def data() -> tuple[list[dict], list[dict], list[dict], dict]:
    incident = load_incident()
    return sorted_events(incident["events"]), load_techniques()["techniques"], load_hypotheses(), incident["metadata"]

events, techniques, hypotheses, metadata = data()
st.session_state.setdefault("mappings", [])
st.session_state.setdefault("recommendations", [])
st.session_state.setdefault("worksheet", hypotheses)

st.markdown('<div class="hero"><h1>Project Nightfall</h1><p>Threat Hunting & ATT&CK Investigation Lab</p><p><i>Investigate the evidence. Map the behaviour. Defend the organisation.</i></p></div>', unsafe_allow_html=True)
st.markdown('<div class="warning">⚠️ <b>SIMULATED EVIDENCE:</b> Every record is fictional and for defensive education. Do not treat this exercise as a real incident.</div>', unsafe_allow_html=True)

st.sidebar.title("Investigation Lab")
st.sidebar.info("Use the pages to move from observation to hypothesis, mapping, and defensible recommendations.")
st.sidebar.caption("MITRE ATT&CK Enterprise v15 • local catalogue • offline after setup")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Evidence records", len(events))
col2.metric("Candidate mappings", len(st.session_state.mappings))
col3.metric("Unresolved questions", sum(not h.get("conclusion") for h in st.session_state.worksheet))
col4.metric("High-confidence observations", sum(e["confidence"] == "High" for e in events))

st.subheader("Incident overview")
st.write("An employee receives an unexpected document-review email. Identity, endpoint, document and network telemetry then produce a timeline with both suspicious and benign explanations. Your job is to separate what is observed from what is inferred.")
st.plotly_chart(timeline_figure(events), use_container_width=True)
st.subheader("Start here")
st.markdown("1. **Incident Timeline** — orient yourself in time.  \n2. **Evidence Explorer** — record observations and limitations.  \n3. **ATT&CK Mapping** — propose only evidence-supported techniques.  \n4. **Threat Hunting** — test hypotheses.  \n5. **Defensive Recommendations** — document controls and telemetry.  \n6. **Export Investigation** — download a Navigator layer and report.")
with st.expander("Data provenance"):
    st.json(metadata)

