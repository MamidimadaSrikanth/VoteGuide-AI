import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_chat_success(client):
    res = client.post("/chat", json={"message": "hello"})
    assert res.status_code == 200
    assert "response" in res.get_json()

def test_chat_bad_request(client):
    res = client.post("/chat", json={"message": ""})
    assert res.status_code == 400

def test_eligibility_success(client):
    res = client.post("/eligibility", json={"age": 20, "citizen": "yes"})
    assert res.status_code == 200

def test_eligibility_invalid_age(client):
    res = client.post("/eligibility", json={"age": -1, "citizen": "yes"})
    assert res.status_code == 400

def test_timeline(client):
    res = client.get("/timeline")
    assert res.status_code == 200