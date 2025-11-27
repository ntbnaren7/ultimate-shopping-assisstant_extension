from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Ultimate Shopping Assistant API is running"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_search_products():
    response = client.post("/api/v1/products/search?query=iphone")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0
    assert data["results"][0]["source"] == "Amazon"

def test_price_history():
    response = client.get("/api/v1/products/123/history")
    assert response.status_code == 200
    data = response.json()
    assert "predicted_price" in data
    assert "confidence_score" in data

def test_review_summary():
    response = client.get("/api/v1/products/123/reviews")
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert "goods" in data["summary"]
