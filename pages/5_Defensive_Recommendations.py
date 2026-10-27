import streamlit as st

st.title("Defensive Recommendations")
st.caption("ATT&CK describes adversary behaviour; MITRE D3FEND organises defensive countermeasure knowledge.")
st.markdown("[Consult the official MITRE D3FEND knowledge base](https://d3fend.mitre.org/). Do not assume a control completely prevents an attack.")
with st.form("recommendation"):
    finding = st.text_input("Related investigative finding")
    action = st.text_input("Proposed defensive action")
    purpose = st.selectbox("Purpose", ["Preventive", "Detective", "Response / containment"])
    telemetry = st.text_input("Telemetry needed to evaluate effectiveness")
    outcome = st.text_input("Expected outcome")
    limitations = st.text_area("Limitations and assumptions")
    reference = st.text_input("Authoritative reference URL", "https://d3fend.mitre.org/")
    if st.form_submit_button("Add recommendation"):
        if not action.strip(): st.error("Provide a defensive action.")
        else:
            st.session_state.recommendations.append({"finding": finding, "action": action, "purpose": purpose, "telemetry": telemetry, "outcome": outcome, "limitations": limitations, "reference": reference})
            st.success("Recommendation added.")
for item in st.session_state.recommendations:
    st.info(f"**{item['purpose']} — {item['action']}**\n\nFinding: {item['finding']}\n\nLimitations: {item['limitations']}")

