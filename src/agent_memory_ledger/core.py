import json
from pathlib import Path

PROJECT = 'Agent Memory Ledger'

def analyze(data):
    items = data.get("items", [])
    ready = [x for x in items if x.get("status") == "ready"]
    review = [x for x in items if x.get("status") == "review"]
    return {
        "ok": True,
        "project": PROJECT,
        "agent_related": True,
        "agent_goal": data.get("goal"),
        "summary": {"items": len(items), "ready": len(ready), "review": len(review)},
        "agent_next_steps": [
            "Inspect structured JSON context",
            "Choose the next safe implementation task",
            "Generate or update code with tests",
            "Return a machine-readable report"
        ],
        "records": items,
    }

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def save(obj, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, indent=2), encoding="utf-8")
    return str(path)
