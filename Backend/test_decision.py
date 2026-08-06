from models.decision import DecisionEngine

engine = DecisionEngine()

sample_batch = {
    "freshness": 90,
    "market_price": 75,
    "demand": 80,
    "logistics": 85,
    "waste_risk": 20,
}

score = engine.score_batch(sample_batch)

print("Decision Score:", score)
print("Recommended Action:", engine.choose_action(score))