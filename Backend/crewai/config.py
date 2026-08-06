import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# API Keys
# ==========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ==========================
# LLM Configuration
# ==========================

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.3-70b-versatile"
)

TEMPERATURE = 0.2

MAX_TOKENS = 2048

# ==========================
# CrewAI Settings
# ==========================

VERBOSE = True

ALLOW_DELEGATION = False

# ==========================
# Decision Engine
# ==========================

VALUE_SCORE_MAX = 100

MIN_CONFIDENCE = 0.70

# ==========================
# Default Weights
# ==========================

WEIGHTS = {
    "freshness": 0.30,
    "market_price": 0.25,
    "demand": 0.20,
    "logistics": 0.15,
    "waste_risk": 0.10
}