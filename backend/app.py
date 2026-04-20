from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel, Field
import uvicorn
import os

from mock_data import get_queue_status, get_crowd_data
from ai_prompts import navigate_prompt, ask_ai_prompt

app = FastAPI(title="AI CrowdSense API")

# Setup CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Efficiency: Compress responses
app.add_middleware(GZipMiddleware, minimum_size=500)

# Security: Add custom security headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

class RouteRequest(BaseModel):
    destination: str = Field(..., max_length=100)

class AskRequest(BaseModel):
    question: str = Field(..., max_length=500)

@app.get("/api/queue-status")
def queue_status():
    """Returns simulated queue status."""
    return get_queue_status()

@app.get("/api/crowd-data")
def crowd_data():
    """Returns simulated crowd data"""
    return get_crowd_data()

@app.post("/api/get-route")
def get_route(req: RouteRequest):
    """Uses AI to find the best route."""
    current_data = get_crowd_data()
    # Call the AI layer
    ai_suggestion = navigate_prompt(req.destination, current_data)
    return {"suggestion": ai_suggestion}

@app.post("/api/ask-ai")
def ask_ai(req: AskRequest):
    """Answers user queries with AI context."""
    q_data = get_queue_status()
    c_data = get_crowd_data()
    
    response = ask_ai_prompt(req.question, q_data, c_data)
    return {"response": response}

# Mount the frontend static files so Cloud Run serves everything from one container
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.isdir(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), reload=True)
