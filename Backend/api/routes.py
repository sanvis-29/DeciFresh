from fastapi import APIRouter, HTTPException

from backend.schemas import BatchRequest, DecisionResponse
from backend.services.orchestrator import process_batch

router = APIRouter(prefix="/api", tags=["DeciFresh AI"])


@router.post("/recommend", response_model=DecisionResponse)
async def recommend(batch: BatchRequest):
    """
    Main endpoint for generating AI recommendations.
    """

    try:
        result = await process_batch(batch)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/health")
async def health():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "service": "DeciFresh AI",
        "version": "1.0"
    }