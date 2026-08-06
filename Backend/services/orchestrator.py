from backend.crewai.crew import run_decifresh
from backend.services.explainability import generate_explanation
from backend.services.counterfactual import generate_counterfactual


async def process_batch(batch):
    """
    Main orchestration service.

    Called by FastAPI.
    """

    # -----------------------------
    # Run CrewAI
    # -----------------------------
    result = run_decifresh(batch.dict())

    # --------------------------------------------------
    # Mock extraction
    # Replace with CrewAI output parsing later
    # --------------------------------------------------

    recommendation = "Move Produce"

    destination = "Gurgaon"

    confidence = 96

    value_score = 94

    reasoning = [
        "Demand increasing",
        "Higher selling price",
        "Traffic is low",
        "Shelf life sufficient"
    ]

    # --------------------------------------------------
    # Human Explanation
    # --------------------------------------------------

    explanation = generate_explanation(
        recommendation=recommendation,
        destination=destination,
        confidence=confidence,
        reasons=reasoning
    )

    # --------------------------------------------------
    # Counterfactual
    # --------------------------------------------------

    counterfactual = generate_counterfactual(
        current_revenue=58000,
        predicted_revenue=82000,
        current_waste_percent=27,
        predicted_waste_percent=4
    )

    # --------------------------------------------------
    # Final API Response
    # --------------------------------------------------

    return {
        "recommendation": {
            "recommended_action": recommendation,
            "destination": destination,
            "confidence": confidence,
            "value_preservation_score": value_score
        },

        "reasoning": reasoning,

        "explanation": explanation,

        "counterfactual": counterfactual
    }