import json
from pathlib import Path
import pytest
from src.data_loader import DataValidationError, load_incident, load_techniques, sorted_events

def test_loads_synthetic_incident():
    incident = load_incident()
    assert incident["metadata"]["synthetic"] is True
    assert len(incident["events"]) >= 6

def test_events_sort_chronologically():
    assert [e["evidence_id"] for e in sorted_events([{"evidence_id":"b","timestamp":"2026-01-02"},{"evidence_id":"a","timestamp":"2026-01-01"}])] == ["a","b"]

def test_rejects_malformed_records(tmp_path: Path):
    path = tmp_path / "bad.json"
    path.write_text(json.dumps({"events": [{"evidence_id": "E-1"}]}), encoding="utf-8")
    with pytest.raises(DataValidationError):
        load_incident(path)

def test_catalogue_is_v15():
    assert load_techniques()["metadata"]["attack_version"] == "v15"

