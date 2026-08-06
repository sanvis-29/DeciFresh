from crewai import Agent
from langchain_openai import ChatOpenAI
import os

# LLM Configuration
llm = ChatOpenAI(
    model="gpt-4o-mini",   # Replace with your preferred model
    temperature=0.2
)

# -----------------------------
# Vision Agent
# -----------------------------

vision_agent = Agent(
    role="Vision Intelligence Agent",

    goal="""
    Analyze the quality of produce and estimate its remaining shelf life.
    """,

    backstory="""
    You are an expert agricultural quality inspector.
    You understand freshness, defects, spoilage indicators,
    and produce grading.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)

# -----------------------------
# Market Agent
# -----------------------------

market_agent = Agent(
    role="Market Intelligence Agent",

    goal="""
    Identify the market that maximizes revenue by analyzing
    demand trends, prices and regional supply.
    """,

    backstory="""
    You specialize in agricultural economics,
    produce pricing and demand forecasting.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)

# -----------------------------
# Logistics Agent
# -----------------------------

logistics_agent = Agent(
    role="Logistics Intelligence Agent",

    goal="""
    Recommend the most efficient transportation plan
    while minimizing delivery time and logistics cost.
    """,

    backstory="""
    You are an expert supply chain planner with
    extensive knowledge of transportation,
    cold chain logistics and route optimization.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)

# -----------------------------
# Institutional Matching Agent
# -----------------------------

institution_agent = Agent(
    role="Institutional Matching Agent",

    goal="""
    Discover alternative high-value destinations
    such as hostels, hospitals, processors,
    cafeterias and NGOs.
    """,

    backstory="""
    You maximize food utilization by matching
    produce with institutions that can use it
    before spoilage.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)

# -----------------------------
# Decision Orchestrator
# -----------------------------

decision_orchestrator = Agent(
    role="Decision Orchestrator",

    goal="""
    Combine insights from all specialist agents,
    compare multiple future scenarios,
    recommend the highest-value action,
    and explain the reasoning.
    """,

    backstory="""
    You are the chief decision maker of DeciFresh.

    You never make assumptions.

    You carefully analyze every specialist report,
    compare all available options,
    choose the best overall strategy,
    and clearly explain why.
    """,

    llm=llm,

    verbose=True,

    allow_delegation=False
)