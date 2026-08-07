from pprint import pprint

from ai_engine.counterfactual import CounterfactualSimulator


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


simulator = CounterfactualSimulator()

result = simulator.simulate(batch)

pprint(result)