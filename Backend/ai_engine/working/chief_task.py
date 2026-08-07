from crewai import Task


def create_chief_task(
    agent,
    quality_task,
    market_task,
    logistics_task,
    sustainability_task,
):
    """
    Creates the Chief Produce Decision task.
    """

    return Task(
        description="""
You are the Chief Produce Decision Officer.

Review the structured reports from:

1. Produce Quality Expert
2. Market Intelligence Analyst
3. Supply Chain & Logistics Expert
4. Sustainability & Food Waste Expert

Using ONLY those specialist reports, choose exactly ONE final business action.

Possible actions:
- Premium Retail
- Standard Retail
- Discount Sale
- Cold Storage
- Food Processing
- Food Donation
- Animal Feed
- Compost

Decision principles:

- Premium Retail requires strong quality AND strong market conditions.
- Standard Retail is preferred when quality is good but premium conditions are not clearly justified.
- Discount Sale is suitable when sale is still viable but value is weakening.
- Cold Storage is appropriate only when delaying sale is justified and waste risk is manageable.
- Food Processing is appropriate when retail quality is insufficient but the produce still has usable value.
- Food Donation is appropriate when commercial value is low but the produce is still edible.
- Animal Feed is appropriate when human consumption is no longer suitable but feed use remains viable.
- Compost is the last-resort option when edible or commercial use is no longer reasonable.

IMPORTANT:
- Do NOT invent new scores or facts.
- Do NOT infer hidden market prices, routes, storage capacity, or shelf life.
- Do NOT choose Premium Retail based on freshness alone.
- Consider all four specialist reports together.
- Return ONLY valid JSON.
""",
        expected_output="""
{
  "final_recommendation": "Premium Retail | Standard Retail | Discount Sale | Cold Storage | Food Processing | Food Donation | Animal Feed | Compost",
  "confidence": 0,
  "primary_factor": "string",
  "reasoning": "string"
}
""",
        agent=agent,
        context=[
            quality_task,
            market_task,
            logistics_task,
            sustainability_task,
        ],
    )