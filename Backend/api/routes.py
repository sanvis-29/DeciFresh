from fastapi import APIRouter, HTTPException, BackgroundTasks
from api.schemas import BatchCreateRequest, DecisionResponse, ProducePassport
from services.orchestrator import evaluate_produce_batch
import uuid

router = APIRouter(prefix="/api/v1", tags=["DeciFresh Backend"])

# In-Memory DB Store for rapid Hackathon demo
BATCH_STORE = {}

@router.post("/batch/evaluate", response_model=DecisionResponse)
async def evaluate_batch(batch: BatchCreateRequest):
    """Triggers multi-agent evaluation and computes highest-value decision."""
    try:
        # Mocking input payload from Member 1's CrewAI kickoff
        agent_raw_inputs = {"location": batch.current_location, "crop": batch.crop_type}
        
        response = evaluate_produce_batch(
            batch_id=batch.batch_id,
            crop_type=batch.crop_type,
            weight_kg=batch.weight_kg,
            agent_raw_inputs=agent_raw_inputs
        )
        
        # Save state to memory store
        BATCH_STORE[batch.batch_id] = {
            "batch_info": batch,
            "latest_decision": response
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/passport/{batch_id}", response_model=ProducePassport)
async def get_digital_passport(batch_id: str):
    """Generates and retrieves the Digital Produce Passport for QR Code scanning."""
    if batch_id not in BATCH_STORE:
        # Default mock fallback for unregistered demo batches
        return ProducePassport(
            passport_id=str(uuid.uuid4())[:8],
            batch_id=batch_id,
            crop_type="Mangoes",
            weight_kg=1000.0,
            origin="Farm A, Azadpur Mandi",
            harvest_date="2026-08-05",
            current_value_preservation_score=92.0,
            quality_grade="Grade A+",
            route_history=["Farm A -> Azadpur Hub", "Azadpur Hub -> Cold Storage 3"],
            qr_code_url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://decifresh.app/passport/{batch_id}"
        )
    
    record = BATCH_STORE[batch_id]
    info = record["batch_info"]
    decision = record["latest_decision"]
    
    return ProducePassport(
        passport_id=str(uuid.uuid4())[:8],
        batch_id=info.batch_id,
        crop_type=info.crop_type,
        weight_kg=info.weight_kg,
        origin=info.origin,
        harvest_date=info.harvest_date,
        current_value_preservation_score=decision.value_preservation_score,
        quality_grade="Grade A+",
        route_history=[info.origin, info.current_location],
        qr_code_url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://decifresh.app/passport/{info.batch_id}"
    )
