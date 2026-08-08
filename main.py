from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router

app = FastAPI(
    title="DeciFresh Backend API",
    description="Decision Layer Engine for Global Fresh Produce Economy",
    version="1.0.0"
)

# Enable CORS for Frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def health_check():
    return {"status": "online", "system": "DeciFresh Decision Engine v1.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)