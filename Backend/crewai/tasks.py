from crewai import Task

from backend.crewai.agents import (
    vision_agent,
    market_agent,
    logistics_agent,
    institution_agent,
    decision_orchestrator,
)

# ==========================================================
# Vision Task
# ==========================================================

vision_task = Task(
    description="""
    Analyze the produce batch.

    Determine:

    - Quality Grade
    - Estimated Shelf Life
    - Visible Defects

    Return ONLY JSON.
    """,

    expected_output="""
    {
        "quality_grade": "",
        "shelf_life_days": 0,
        "confidence": 0
    }
    """,

    agent=vision_agent,
)

# ==========================================================
# Market Task
# ==========================================================

market_task = Task(
    description="""
    Analyze the current market.

    Determine:

    - Best Market
    - Current Price
    - Demand Trend

    Return ONLY JSON.
    """,

    expected_output="""
    {
        "best_market": "",
        "price_per_kg": 0,
        "demand": "",
        "confidence": 0
    }
    """,

    agent=market_agent,
)

# ==========================================================
# Logistics Task
# ==========================================================

logistics_task = Task(
    description="""
    Evaluate transportation options.

    Determine:

    - Delivery Time
    - Logistics Cost
    - Route Risk

    Return ONLY JSON.
    """,

    expected_output="""
    {
        "delivery_time_hours": 0,
        "transport_cost": 0,
        "route_risk": "",
        "confidence": 0
    }
    """,

    agent=logistics_agent,
)

# ==========================================================
# Institution Task
# ==========================================================

institution_task = Task(
    description="""
    Search for institutional buyers.

    Consider:

    - Hospitals
    - Universities
    - Hostels
    - NGOs
    - Juice Processors

    Return ONLY JSON.
    """,

    expected_output="""
    {
        "destination": "",
        "quantity": 0,
        "priority": "",
        "confidence": 0
    }
    """,

    agent=institution_agent,
)

# ==========================================================
# Decision Task
# ==========================================================

decision_task = Task(
    description="""
    Collect the outputs from all specialist agents.

    Compare all possible future scenarios.

    Select the highest-value action.

    Explain your reasoning.

    Perform counterfactual analysis.

    Calculate the Value Preservation Score.

    Return ONLY JSON.
    """,

    expected_output="""
    {
        "recommended_action": "",
        "destination": "",
        "confidence": 0,
        "value_preservation_score": 0,
        "reasoning": [],
        "counterfactual": {
            "revenue_without_action": 0,
            "revenue_with_action": 0,
            "waste_without_action": 0,
            "waste_with_action": 0
        }
    }
    """,

    agent=decision_orchestrator,
)