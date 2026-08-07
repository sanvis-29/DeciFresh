from pprint import pprint

from ai_engine.orchestrator import run_decifresh


# ============================================================
# SUPER STRESS-TEST BATCH
# ============================================================

batch = {
    "batch_id": "SP-999",
    "produce_type": "Spinach",
    "quantity_kg": 500,

    # Very poor condition
    "freshness": 20,

    # Weak commercial opportunity
    "market_price": 25,
    "demand": 25,

    # Difficult logistics
    "logistics": 30,

    # Extremely high waste risk
    "waste_risk": 90,
}


print("\n==========================================")
print("       DECIFRESH SUPER STRESS TEST")
print("==========================================")

print(f"Batch: {batch['batch_id']}")
print(f"Produce: {batch['produce_type']}")
print(f"Freshness: {batch['freshness']}")
print(f"Market Price: {batch['market_price']}")
print(f"Demand: {batch['demand']}")
print(f"Logistics: {batch['logistics']}")
print(f"Waste Risk: {batch['waste_risk']}")

print("==========================================\n")


# ============================================================
# RUN DECIFRESH
# ============================================================

result = run_decifresh(batch)


# ============================================================
# FINAL RESULT
# ============================================================

print("\n==========================================")
print("           FINAL TEST RESULT")
print("==========================================\n")

pprint(result)

print("\n==========================================")