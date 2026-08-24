from fastapi.testclient import TestClient
from lect27 import app   # 👈 file name = api.py

client = TestClient(app)


# 🔹 Test Home Endpoint
def test_home():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Mayank"}


# 🔹 Test Add Endpoint
def test_add():
    response = client.get("/add?a=5&b=5")
    
    assert response.status_code == 200
    assert response.json() == {"result": 10}


# 🔹 Edge Case (important 🔥)
def test_add_invalid():
    response = client.get("/add?a=5&b=abc")  # invalid input
    
    assert response.status_code == 422   # FastAPI validation error