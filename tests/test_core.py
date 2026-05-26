from agent_memory_ledger.core import analyze

def test_analyze_marks_agent_related():
    result = analyze({"goal":"x", "items":[{"id":"1", "status":"ready"}]})
    assert result["ok"] is True
    assert result["agent_related"] is True
    assert result["summary"]["items"] == 1
