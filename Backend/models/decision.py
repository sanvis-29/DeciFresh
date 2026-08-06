from pydantic import BaseModel
from typing import List


class AlternativeDecision(BaseModel):
    action: str
    destination: str
    expected_revenue: float
    expected_waste_percent: float
    confidence: float
    score: float


class Counterfactual(BaseModel):
    revenue_without_action: float
    revenue_with_action: float
    waste_without_action: float
    waste_with_action: float
    meals_saved: int
    co2_saved_kg: float


class Decision(BaseModel):
    recommended_action: str
    destination: str

    confidence: float

    value_preservation_score: float

    reasoning: List[str]

    alternatives: List[AlternativeDecision]

    counterfactual: Counterfactual