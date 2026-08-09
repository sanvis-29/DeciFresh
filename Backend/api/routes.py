from fastapi import APIRouter, HTTPException

from Backend.api.schemas import (
    BatchCreateRequest,
    DecisionResponse,
    ProducePassport,
)

from Backend.services.decision_service import process_decision


router = APIRouter(
    prefix="/api",
    tags=["DeciFresh"],
)


@router.get("/health")
def api_health():
    return {
        "status": "online",
        "service": "DeciFresh API",
    }


@router.post("/decision")
def create_decision(batch: BatchCreateRequest):
    """
    Run the complete DeciFresh intelligence pipeline.
    """

    try:
        batch_data = batch.model_dump()

        result = process_decision(batch_data)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post("/passport")
def create_passport(batch: BatchCreateRequest):
    """
    Generate a digital produce passport containing
    the DeciFresh decision intelligence.
    """

    try:
        batch_data = batch.model_dump()

        result = process_decision(batch_data)

        passport = {
            "batch_id": result.get("batch_id"),
            "produce_type": result.get("produce_type"),
            "quantity_kg": result.get("quantity_kg"),

            "decision_engine": result.get(
                "decision_engine"
            ),

            "counterfactual_analysis": result.get(
                "counterfactual_analysis"
            ),

            "historical_matches": result.get(
                "historical_matches"
            ),

            "ai_decision": result.get(
                "ai_decision"
            ),
        }

        return passport

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )