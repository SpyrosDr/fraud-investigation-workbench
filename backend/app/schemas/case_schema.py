from pydantic import BaseModel, Field


class CaseInput(BaseModel):
    context: str
    description: str
    evidence_items: list[str] = Field(default_factory=list)

class CaseAssessmentResponse(BaseModel):
    provider: str
    case_context: str
    risk_level: str
    risk_indicators: list[str]
    next_steps: list[str]
    draft_summary: str
