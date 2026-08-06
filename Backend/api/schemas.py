from pydantic import BaseModel, Field
from typing import List, Optional


# ---------- Incoming Request ----------

class BatchRequest(BaseModel):
    batch_id: str = Field(..., example="MX-201")
    produce_type: str = Field(..., example="Mango")
    quantity_kg: float = Field(..., example=1000)
    location: str = Field(..., example="Delhi")

    # Optional if Computer Vision hasn't run yet
    quality_grade: Optional[str] = None
    estimated_shelf_life_days: Optional[int] = None


# ---------- AI Recommendation ----------

class Recommendation(BaseModel):
    recommended_action: str
    destination: str
    confidence: float
    value_preservation_score: float


# ---------- Alternative Futures ----------

class AlternativeDecision(BaseModel):
    action: str
    expected_revenue: float
    expected_waste_percent: float
    score: float


# ---------- Counterfactual ----------

class Counterfactual(BaseModel):
    revenue_without_action: float
    revenue_with_action: float

    waste_without_action: float
    waste_with_action: float

    meals_saved: int
    co2_saved_kg: float


# ---------- Final Response ----------

class DecisionResponse(BaseModel):
    recommendation: Recommendation

    reasoning: List[str]

    alternatives: List[AlternativeDecision]

    counterfactual: Counterfactual