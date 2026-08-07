from pprint import pprint

from ai_engine.orchestrator import run_decifresh


# =========================================================
# DECIFRESH HISTORICAL RAG + COUNTERFACTUAL INTEGRATION TEST
# =========================================================

batch = {
    "batch_id": "RAG-TEST-001",
    "produce_type": "Mango",
    "quantity_kg": 1000,

    "freshness": 86,
    "market_price": 76,
    "demand": 80,
    "logistics": 84,
    "waste_risk": 20,
}


print("\n" + "=" * 60)
print("        DECIFRESH FULL INTELLIGENCE TEST")
print("=" * 60)

print(f"Batch: {batch['batch_id']}")
print(f"Produce: {batch['produce_type']}")
print(f"Freshness: {batch['freshness']}")
print(f"Market Price: {batch['market_price']}")
print(f"Demand: {batch['demand']}")
print(f"Logistics: {batch['logistics']}")
print(f"Waste Risk: {batch['waste_risk']}")

print("=" * 60)

result = run_decifresh(batch)

print("\n")
print("=" * 60)
print("              FINAL DECIFRESH RESULT")
print("=" * 60)

pprint(result)

print("=" * 60)