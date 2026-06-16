from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="AI-Assisted Fraud Investigation Workbench",
    description="MVP backend for structured fraud investigation support.",
    version="0.1.0",
)


class CaseInput(BaseModel):
    context: str
    description: str
    evidence_items: Optional[List[str]] = []


@app.get("/")
def read_root():
    return {
        "message": "Fraud Investigation Workbench API is running"
    }


@app.post("/assess-case")
def assess_case(case: CaseInput):
    risk_indicators = []

    text = f"{case.context} {case.description} {' '.join(case.evidence_items)}".lower()

    if "invoice" in text or "vendor" in text:
        risk_indicators.append("Possible vendor or procurement fraud indicators")

    if "account" in text or "login" in text:
        risk_indicators.append("Possible account takeover or identity-related indicators")

    if "cash" in text or "transfer" in text or "transaction" in text:
        risk_indicators.append("Possible suspicious financial movement indicators")

    if not risk_indicators:
        risk_indicators.append("No clear predefined fraud indicators detected yet")

    return {
        "case_context": case.context,
        "risk_level": "medium" if len(risk_indicators) >= 2 else "low",
        "risk_indicators": risk_indicators,
        "next_steps": [
            "Collect supporting evidence",
            "Identify involved entities",
            "Build a timeline of events",
            "Document assumptions and open questions"
        ],
        "draft_summary": f"Initial review of the case suggests: {', '.join(risk_indicators)}."
    }
