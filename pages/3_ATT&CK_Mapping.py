import streamlit as st
from app import data
from src.attack_mapper import add_mapping, search_techniques, update_status

events, techniques, _, _ = data()
st.title("ATT&CK Mapping Workspace")
st.caption("Candidate mappings are analyst assessments, not official MITRE classifications.")
event_id = st.selectbox("Evidence record", [e["evidence_id"] for e in events])
q = st.text_input("Search technique ID or name")
tactic = st.selectbox("Tactic", ["All"] + sorted({t["tactic"] for t in techniques}))
matches = search_techniques(techniques, q, tactic)
if not matches:
    st.warning("No local v15 technique matches.")
else:
    selected_id = st.selectbox("Technique", [t["technique_id"] + " — " + t["name"] for t in matches])
    selected = next(t for t in matches if t["technique_id"] == selected_id.split(" — ")[0])
    st.info(f"**{selected['tactic']}** — {selected['description']}")
    with st.form("mapping"):
        evidence_ids = st.multiselect("Supporting evidence IDs", [e["evidence_id"] for e in events], default=[event_id])
        rationale = st.text_area("Analyst rationale (required for supported status)")
        alternatives = st.text_area("Alternative explanations")
        missing = st.text_area("Missing evidence")
        confidence = st.select_slider("Analyst confidence", ["Low", "Medium", "High"], value="Medium")
        status = st.selectbox("Assessment status", ["proposed", "further_investigation", "supported", "rejected"])
        if st.form_submit_button("Add candidate mapping"):
            try:
                add_mapping(st.session_state.mappings, {"technique_id": selected["technique_id"], "evidence_ids": evidence_ids, "rationale": rationale, "alternative_explanations": alternatives, "missing_evidence": missing, "confidence": confidence, "status": status}, techniques)
                st.success("Mapping added to this session.")
            except ValueError as exc:
                st.error(str(exc))
st.subheader("Current mappings")
for index, mapping in enumerate(st.session_state.mappings):
    with st.expander(f"{mapping['technique_id']} {mapping['technique_name']} · {mapping['status']}"):
        st.write(mapping)
        new_status = st.selectbox("Update status", ["proposed", "further_investigation", "supported", "rejected"], index=["proposed", "further_investigation", "supported", "rejected"].index(mapping["status"]), key=f"status_{index}")
        if st.button("Save status", key=f"save_{index}"):
            try: update_status(mapping, new_status); st.rerun()
            except ValueError as exc: st.error(str(exc))

