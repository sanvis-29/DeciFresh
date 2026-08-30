import os
from dotenv import load_dotenv
from crewai import LLM
import crewai.llms.cache as _crewai_cache
_crewai_cache.mark_cache_breakpoint = lambda msg: msg

load_dotenv("Backend/.env")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "groq/openai/gpt-oss-120b"
)

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)

VERBOSE = True
ALLOW_DELEGATION = False

VALUE_SCORE_MAX = 100
MIN_CONFIDENCE = 0.70

WEIGHTS = {
    "freshness": 0.30,
    "market_price": 0.25,
    "demand": 0.20,
    "logistics": 0.15,
    "waste_risk": 0.10,
}