from src.report_generator import generate_report
from src.validation import validate_events

def test_duplicate_ids_are_reported():
    assert validate_events([{"evidence_id":"E-1","timestamp":"x"},{"evidence_id":"E-1","timestamp":"y"}])

def test_report_is_simulated_and_contains_sections():
    report = generate_report([], [], [], [])
    assert "SIMULATED TRAINING CASE" in report
    assert "Data provenance" in report

