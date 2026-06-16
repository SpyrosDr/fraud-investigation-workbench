from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Fraud Investigation Workbench API is running"


def test_assess_case():
    response = client.post(
        "/assess-case",
        json={
            "context": "Auditor reviewing possible vendor misuse",
            "description": "Several invoices were submitted by a new vendor.",
            "evidence_items": ["invoice 1001", "vendor bank account"]
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] in ["low", "medium"]
    assert "risk_indicators" in data
    assert "next_steps" in data
    assert "draft_summary" in data
