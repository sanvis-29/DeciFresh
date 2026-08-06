from crewai import Agent, Task, Crew, Process
from ai_engine.config import llm   # or your correct import

agent = Agent(
    role="Test Agent",
    goal="Answer simple questions",
    backstory="You are a helpful AI assistant.",
    llm=llm
)

task = Task(
    description="Explain what mangoes are in one sentence.",
    expected_output="A one sentence explanation.",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential
)

print(crew.kickoff())