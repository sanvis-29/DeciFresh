from crewai import Task
from ai_engine.agents import (
    market_agent,
    logistics_agent,
    vision_agent,
    decision_agent,
    counterfactual_agent,
    explainability_agent,
)

from ai_engine.prompts import (
    MARKET_PROMPT,
    LOGISTICS_PROMPT,
    VISION_PROMPT,
    DECISION_PROMPT,
    COUNTERFACTUAL_PROMPT,
    EXPLAINABILITY_PROMPT,
)


vision_task = Task(
    description=VISION_PROMPT,
    expected_output="Quality assessment",
    agent=vision_agent,
)

market_task = Task(
    description=MARKET_PROMPT,
    expected_output="Market prediction",
    agent=market_agent,
)

logistics_task = Task(
    description=LOGISTICS_PROMPT,
    expected_output="Route recommendation",
    agent=logistics_agent,
)

decision_task = Task(
    description=DECISION_PROMPT,
    expected_output="Final decision",
    agent=decision_agent,
)

counterfactual_task = Task(
    description=COUNTERFACTUAL_PROMPT,
    expected_output="Loss estimate",
    agent=counterfactual_agent,
)

explainability_task = Task(
    description=EXPLAINABILITY_PROMPT,
    expected_output="Human-readable explanation",
    agent=explainability_agent,
)