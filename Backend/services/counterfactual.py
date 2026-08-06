from typing import Dict


def generate_counterfactual(
    current_revenue: float,
    predicted_revenue: float,
    current_waste_percent: float,
    predicted_waste_percent: float,
):
    """
    Compare the recommended action against doing nothing.
    """

    revenue_saved = predicted_revenue - current_revenue

    waste_prevented = (
        current_waste_percent - predicted_waste_percent
    )

    # Approximation
    meals_saved = int(max(0, waste_prevented * 30))

    # Approximation
    co2_saved = round(waste_prevented * 22.5, 2)

    return {
        "revenue_without_action": current_revenue,
        "revenue_with_action": predicted_revenue,
        "revenue_saved": revenue_saved,

        "waste_without_action": current_waste_percent,
        "waste_with_action": predicted_waste_percent,
        "waste_prevented": waste_prevented,

        "meals_saved": meals_saved,

        "co2_saved_kg": co2_saved
    }