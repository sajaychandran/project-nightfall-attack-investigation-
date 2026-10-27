from src.navigator_export import build_layer, validate_layer

def test_layer_metadata_and_annotations():
    layer = build_layer([{"technique_id":"T1057","evidence_ids":["E-04"],"rationale":"Process query observed.","status":"proposed","confidence":"High"}])
    validate_layer(layer)
    assert layer["domain"] == "enterprise-attack"
    assert layer["versions"]["attack"] == "15"
    assert "E-04" in layer["techniques"][0]["comment"]

def test_empty_investigation_exports():
    layer = build_layer([])
    validate_layer(layer)
    assert layer["techniques"] == []

