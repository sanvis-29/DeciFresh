from crewai import Agent, Task, Crew, Process
from ai_engine.config import llm
from models.decision import DecisionEngine

# -----------------------------
# Initialize Decision Engine
# -----------------------------
engine = DecisionEngine()

# Sample Produce Batch
batch = {
    "freshness": 90,
    "market_price": 75,
    "demand": 80,
    "logistics": 85,
    "waste_risk": 20,
}

# -----------------------------
# Decision Engine Output
# -----------------------------
score = engine.score_batch(batch)
action = engine.choose_action(score)

print("\n========== DECISION ENGINE ==========")
print(f"Score: {score}")
print(f"Recommended Action: {action}")
print("=====================================\n")

# -----------------------------
# CrewAI Agent
# -----------------------------
agent = Agent(
    role="Produce Decision Analyst",
    goal="Analyze produce batches and determine the best business decision.",
    backstory=(
        "You are an AI expert specializing in fresh produce supply chains, "
        "food waste reduction, pricing strategy, logistics optimization, "
        "and sustainability."
    ),
    llm=llm,
    verbose=True,
)

# -----------------------------
# Task
# -----------------------------
task = Task(
    description=f"""
You are an AI produce decision expert.

A produce batch has the following characteristics:

Freshness: {batch['freshness']}
Market Price: {batch['market_price']}
Demand: {batch['demand']}
Logistics: {batch['logistics']}
Waste Risk: {batch['waste_risk']}

The Decision Engine calculated an overall score of:

Score: {score}

Use this information to independently determine the BEST business decision.

Possible actions:

- Premium Retail
- Standard Retail
- Discount Sale
- Cold Storage
- Food Processing
- Food Donation
- Animal Feed
- Compost

Return your response in the following format:

Recommended Action:
Confidence:
Reasoning:
""",
    expected_output="""
Recommended Action
Confidence
Reasoning
""",
    agent=agent,
)

# -----------------------------
# Crew
# -----------------------------
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
)

# -----------------------------
# Execute
# -----------------------------
print("========== AI DECISION ==========\n")
result = crew.kickoff()

print(result)