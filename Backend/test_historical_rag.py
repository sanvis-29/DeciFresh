from pprint import pprint

from ai_engine.historical_rag import HistoricalRAG


batch = {
    "batch_id": "NEW-001",
    "produce_type": "Mango",
    "freshness": 85,
    "market_price": 74,
    "demand": 80,
    "logistics": 83,
    "waste_risk": 22,
}


rag = HistoricalRAG()

matches = rag.retrieve_similar(
    batch,
    top_k=3
)

print("\nMOST SIMILAR HISTORICAL BATCHES\n")

pprint(matches)