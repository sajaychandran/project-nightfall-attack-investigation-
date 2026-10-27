import streamlit as st
from app import data

_, _, hypotheses, _ = data()
st.title("Threat Hunting Worksheet")
st.caption("These are synthetic questions and procedures, not live SIEM queries.")
for index, original in enumerate(hypotheses):
    item = st.session_state.worksheet[index]
    with st.expander(f"{item['hypothesis_id']} · {item['question']}", expanded=index == 0):
        st.write("**Supporting observations:**", item["supporting_observations"])
        st.write("**Contradicting evidence:**", item["contradicting_evidence"])
        st.write("**Procedure:**", item["procedure"])
        item["findings"] = st.text_area("Findings", item.get("findings", ""), key=f"findings_{index}")
        item["conclusion"] = st.text_area("Conclusion (leave blank if unresolved)", item.get("conclusion", ""), key=f"conclusion_{index}")
        item["confidence"] = st.selectbox("Confidence", ["Unassessed", "Low", "Medium", "High"], index=["Unassessed","Low","Medium","High"].index(item.get("confidence", "Unassessed")), key=f"hc_{index}")
        item["next_action"] = st.text_input("Next investigative action", item.get("next_action", ""), key=f"next_{index}")

