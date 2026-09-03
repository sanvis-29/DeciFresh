# 🌱 DeciFresh

### AI-Powered Decision Intelligence for Fresh Produce Supply Chains

> **Every batch has multiple futures. DeciFresh helps choose the one that preserves the most value.**

Fresh produce decisions are time-sensitive. A batch that is suitable for retail today may need to be redirected to processing tomorrow. Delayed or poorly informed decisions can mean lost revenue, unnecessary waste, and inefficient logistics.

**DeciFresh** is an AI-driven produce decision intelligence platform that evaluates the current state of a produce batch, simulates its possible futures, learns from historical outcomes, and recommends the most valuable next action.

Instead of simply asking:

> *“Is this produce fresh?”*

DeciFresh asks:

> **“Given its quality, market conditions, logistics, demand, and waste risk — what should happen to this batch next?”**

---

## 🚀 What DeciFresh Does

For every produce batch, DeciFresh combines:

- 📷 **AI Vision Analysis**
- 🧮 **Deterministic Decision Scoring**
- 🤖 **Multi-Agent AI Reasoning**
- 🔮 **Counterfactual Future Simulation**
- 📚 **Historical Intelligence**
- ✅ **Independent Decision Validation**
- 🪪 **Digital Produce Passport**

to recommend the best destination for the batch.

Possible outcomes include:

| Action | Purpose |
|---|---|
| 🏪 Premium Retail | High-quality produce with strong market potential |
| 🛒 Standard Retail | Produce suitable for regular retail channels |
| ❄️ Cold Storage | Preserve value when delaying sale is beneficial |
| 🏷️ Discount Sale | Accelerate movement of time-sensitive produce |
| 🏭 Food Processing | Redirect produce into processed products |
| ❤️ Food Donation | Recover usable produce for social value |
| 🐄 Animal Feed | Recover residual value from unsuitable produce |
| ♻️ Compost | Responsible end-of-life recovery |

---

# 💡 The Problem

Fresh produce supply chains operate under severe time pressure.

A warehouse or distributor must continuously decide whether produce should be:

**sold, stored, discounted, processed, donated, redirected, or discarded.**

But these decisions are often fragmented across visual inspection, experience, market information, logistics constraints, and isolated software systems.

This creates three major problems:

### 1. Decisions are reactive

Produce may deteriorate before action is taken.

### 2. The future value of alternative actions is unclear

Choosing retail over processing, or storage over immediate sale, has different economic and waste implications.

### 3. Valuable operational knowledge gets lost

Historical batches may contain useful evidence, but that experience is rarely incorporated systematically into the next decision.

---

# 🌿 The DeciFresh Approach

DeciFresh treats produce routing as a **decision intelligence problem**.

```text
                 PRODUCE BATCH
                       │
                       ▼
              ┌─────────────────┐
              │   AI VISION     │
              │ Quality Analysis│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ DECISION ENGINE │
              │ Baseline Scoring│
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   Historical      Specialist   Counterfactual
   Intelligence      Agents       Simulator
          │            │            │
          └────────────┼────────────┘
                       ▼
                ┌─────────────┐
                │ CHIEF AGENT │
                │ Final Reason│
                └──────┬──────┘
                       ▼
                ┌─────────────┐
                │  VALIDATOR  │
                │ Audit Result│
                └──────┬──────┘
                       ▼
               FINAL RECOMMENDATION
                       │
                       ▼
             DIGITAL PRODUCE PASSPORT
```

---

# ✨ Core Features

## 📷 1. AI Vision Inspection

Upload an image of a produce sample.

DeciFresh's vision pipeline analyzes visible characteristics and returns structured information such as:

- Produce type
- Freshness score
- Quality grade
- Visible issues
- Confidence
- Visual condition summary

The result becomes an input into the wider decision pipeline rather than acting as the final decision itself.

---

## 🧮 2. Deterministic Decision Engine

DeciFresh maintains a deterministic baseline alongside generative AI reasoning.

The engine evaluates factors such as:

```text
Freshness
Market Price
Demand
Logistics
Waste Risk
```

using weighted decision logic.

This provides a reproducible baseline against which AI recommendations can be compared.

---

## 🤖 3. Multi-Agent Decision Intelligence

DeciFresh uses a **CrewAI-based specialist architecture** rather than relying on a single AI prompt.

Specialist perspectives evaluate the batch from different operational viewpoints:

### Quality Intelligence
Evaluates freshness, quality, deterioration, and suitability.

### Market Intelligence
Considers demand, pricing conditions, and commercial opportunity.

### Logistics Intelligence
Evaluates operational feasibility and movement constraints.

### Sustainability Intelligence
Considers waste prevention and responsible recovery pathways.

Their findings are synthesized by a **Chief Produce Decision Agent**.

---

## 🔮 4. Counterfactual Future Simulator

DeciFresh doesn't evaluate only one recommendation.

It asks:

> **“What happens if we choose each possible action?”**

The simulator evaluates alternative futures such as:

```text
Premium Retail
Standard Retail
Cold Storage
Discount Sale
Food Processing
Food Donation
Animal Feed
Compost
```

For each scenario, DeciFresh estimates a **Future Value** and compares it against the baseline.

This makes the system capable of answering not only:

> “What should we do?”

but also:

> **“Why is this action better than the alternatives?”**

---

## 📚 5. Historical Intelligence

DeciFresh retrieves similar historical produce batches and their outcomes.

Relevant past cases can include:

- Produce characteristics
- Freshness
- Market conditions
- Demand
- Logistics
- Waste risk
- Previous decision
- Actual outcome
- Waste percentage

Historical evidence is supplied to the AI reasoning layer so decisions are grounded in comparable outcomes rather than generated in isolation.

---

## 🧠 6. Chief Decision Agent

Specialist analysis, historical evidence, counterfactual simulations, and the deterministic engine are brought together by the **Chief Produce Decision Agent**.

It generates:

- Final recommendation
- Confidence
- Decision reasoning
- Comparison with the deterministic engine

---

## ✅ 7. Independent Validation Layer

AI-generated recommendations are passed through an additional validation stage.

The validator checks for:

- Unsupported claims
- Contradictions
- Misinterpretation of available evidence
- Agreement with specialist findings
- Consistency with the deterministic engine

The final output includes a validation status such as:

```text
APPROVED
```

along with engine-agreement information.

This creates an **AI proposes → AI audits → system reports** workflow.

---

## 🪪 8. Digital Produce Passport

Every analyzed batch can be represented through a Digital Produce Passport containing its decision intelligence.

The passport can include:

- Batch identity
- Produce type
- Quantity
- Decision score
- Recommended action
- Counterfactual analysis
- Historical matches
- AI recommendation
- Confidence
- Validation result

This creates a traceable decision record for the batch.

---

# 🔄 End-to-End Pipeline

```text
1. Produce batch is registered
        ↓
2. Produce image is analyzed
        ↓
3. Batch attributes enter the Decision Engine
        ↓
4. Deterministic baseline is calculated
        ↓
5. Alternative futures are simulated
        ↓
6. Similar historical cases are retrieved
        ↓
7. Specialist AI agents analyze the batch
        ↓
8. Chief Agent synthesizes the evidence
        ↓
9. Validator audits the recommendation
        ↓
10. Final decision is returned
        ↓
11. Digital Produce Passport is generated
```

---

# 🛠️ Technology Stack

### Backend

- **Python**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

### AI & Agentic Intelligence

- **CrewAI**
- **Groq**
- **LiteLLM**
- **LangChain**

### Computer Vision

- Multimodal LLM-based produce inspection
- Pillow for image handling

### Frontend

- **HTML**
- **CSS**
- **JavaScript**

### Decision Intelligence

- Custom deterministic scoring engine
- Counterfactual simulation
- Historical similarity retrieval
- Multi-agent reasoning
- Validation layer

---

# 🏗️ Project Architecture

```text
DeciFresh/
│
├── Backend/
│   │
│   ├── ai_engine/
│   │   ├── agents.py
│   │   ├── config.py
│   │   ├── crew.py
│   │   ├── orchestrator.py
│   │   └── ...
│   │
│   ├── api/
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── ...
│   │
│   ├── services/
│   │   ├── decision_service.py
│   │   ├── vision_service.py
│   │   └── ...
│   │
│   └── ...
│
├── Frontend/
│   └── decifresh.html/
│       └── decifresh_f.html
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The exact internal structure may evolve as DeciFresh is expanded.

---

# ⚙️ Running DeciFresh Locally

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd DeciFresh
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your `.env` file or API credentials.

---

## 5. Start the backend

From the project root:

```bash
uvicorn main:app --reload
```

The API will run locally on port `8000`.

FastAPI's interactive API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## 6. Start the frontend

Open another terminal from the project root:

```bash
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500/Frontend/decifresh.html/decifresh_f.html
```

Keep both the backend and frontend terminals running.

---

# 🔌 API Endpoints

## Health Check

```http
GET /api/health
```

Checks whether the DeciFresh API is operational.

---

## Produce Vision Analysis

```http
POST /api/vision/analyze
```

Analyzes an uploaded produce image and returns structured visual intelligence.

Example output:

```json
{
  "produce_type": "Apple",
  "freshness_score": 68,
  "quality_grade": "Standard",
  "visible_issues": [
    "minor surface blemishes",
    "light discoloration"
  ],
  "confidence": 90,
  "visual_summary": "The produce remains suitable for standard retail."
}
```

---

## Decision Intelligence

```http
POST /api/decision
```

Example request:

```json
{
  "batch_id": "MX-201",
  "crop_type": "Mangoes",
  "weight_kg": 1000,
  "origin": "Farm A",
  "harvest_date": "2026-08-05",
  "current_location": "Delhi Warehouse",
  "vision_freshness": 70
}
```

The response contains:

```text
Decision Engine
Counterfactual Analysis
Historical Matches
AI Decision
Validation Status
Confidence
Reasoning
```

---

## Digital Produce Passport

```http
POST /api/passport
```

Generates the decision-intelligence record associated with a produce batch.

---

# 🧪 Example Decision Flow

Consider a batch of mangoes entering a warehouse.

DeciFresh may determine:

```text
Decision Engine
Score: 54.5
Recommendation: Food Processing

AI Decision
Final Recommendation: Food Processing
Confidence: 93%

Validation
Status: APPROVED
Engine Agreement: AGREE
```

At the same time, the counterfactual engine evaluates what would happen if the batch were instead sent to retail, cold storage, discount sale, donation, animal feed, or compost.

The operator therefore receives a **decision with alternatives and evidence**, rather than a single unexplained classification.

---

# 🎯 Why DeciFresh Is Different

Many food-tech systems focus on one part of the problem:

```text
Freshness Detection
        OR
Demand Forecasting
        OR
Inventory Management
        OR
Waste Tracking
```

DeciFresh focuses on the **decision between them**.

Its core question is:

> **What is the highest-value future available to this batch right now?**

The system combines deterministic computation with agentic reasoning rather than treating an LLM as the sole decision-maker.

---

# 📈 Business Model

DeciFresh is designed as a **B2B SaaS platform** for:

- Produce warehouses
- Distributors
- Wholesalers
- Retail supply chains
- Food processors
- Aggregators
- Large produce networks

The platform is designed around subscription-based decision intelligence rather than commissions on produce transactions.

### Planned Pricing

| Plan | Price | Designed For |
|---|---:|---|
| **Starter** | ₹1,499/month | Small warehouses and early deployments |
| **Growth** | ₹4,999/month | Growing produce operations |
| **Enterprise** | Custom | Multi-location and integrated supply chains |

Potential enterprise capabilities include ERP/WMS integration, custom decision policies, role-based teams, multi-region operations, and advanced analytics.

---

# 🌍 Expected Impact

DeciFresh aims to help produce networks:

**Reduce avoidable food waste** by acting before deterioration eliminates valuable alternatives.

**Preserve economic value** by comparing multiple possible destinations instead of defaulting to disposal or rushed sales.

**Improve decision consistency** through deterministic scoring, historical evidence, and AI validation.

**Make decisions explainable** by showing why an action was recommended and how alternatives compare.

**Build operational intelligence over time** by preserving decision and outcome histories.

---

# 🗺️ Future Roadmap

Future development can extend DeciFresh with:

- Real-time market price feeds
- Weather intelligence
- Cold-chain sensor integration
- ERP/WMS integrations
- Dynamic shelf-life prediction
- Larger historical knowledge bases
- Multi-warehouse optimization
- Role-based operational dashboards
- Decision-outcome feedback loops
- Advanced waste and value analytics

---

# 🔐 Security

API keys and other secrets should be stored only through environment variables.

Do **not** commit:

```text
.env
API keys
Credentials
Private configuration
```

---

# 🤝 Contributing

Contributions, experiments, and improvements are welcome.

A typical workflow:

```bash
git checkout -b feature/your-feature
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

Then open a pull request describing the change.

---

# 🌱 DeciFresh

### From freshness detection to decision intelligence.

**See the batch. Simulate its futures. Preserve its value.**
