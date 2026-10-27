import pytest
from src.attack_mapper import add_mapping, search_techniques, update_status, validate_technique
from src.data_loader import load_techniques

TECHNIQUES = load_techniques()["techniques"]

def test_search_by_id_and_tactic():
    assert search_techniques(TECHNIQUES, "T1057")[0]["name"] == "Process Discovery"
    assert all(t["tactic"] == "Discovery" for t in search_techniques(TECHNIQUES, tactic="Discovery"))

def test_invalid_id_rejected():
    with pytest.raises(ValueError): validate_technique(TECHNIQUES, "T9999")

def test_mapping_requires_evidence_and_rationale():
    with pytest.raises(ValueError): add_mapping([], {"technique_id":"T1057","evidence_ids":[],"rationale":""}, TECHNIQUES)

def test_supported_requires_rationale():
    mapping = {"status":"proposed", "rationale":""}
    with pytest.raises(ValueError): update_status(mapping, "supported")

