import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_queue_status():
    response = client.get("/api/queue-status")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "stall" in data[0]
        assert "wait" in data[0]

def test_crowd_data():
    response = client.get("/api/crowd-data")
    assert response.status_code == 200
    data = response.json()
    # It should have a mapping of gates
    assert isinstance(data, dict)
    assert "Gate 1" in data

def test_get_route_validation():
    # Test pydantic validation is working
    response = client.post("/api/get-route", json={})
    assert response.status_code == 422 # Unprocessable Entity
    
    response = client.post("/api/get-route", json={"destination": "A" * 150})
    assert response.status_code == 422 # Unprocessable Entity (max length 100)

def test_ask_ai_validation():
    response = client.post("/api/ask-ai", json={"question": "A" * 600})
    assert response.status_code == 422 # Unprocessable Entity (max length 500)
