from pprint import pprint

from ai_engine.orchestrator import run_decifresh


batch = {
    "batch_id": "MX-201",
    "produce_type": "Mango",
    "quantity_kg": 1000,

    "freshness": 90,
    "market_price": 75,
    "demand": 80,
    "logistics": 85,
    "waste_risk": 20,
}


result = run_decifresh(batch)

print("\n==========================================")
print("         DECIFRESH FINAL RESPONSE")
print("==========================================\n")

pprint(result)