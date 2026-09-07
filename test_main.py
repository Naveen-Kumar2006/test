from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "House Price Prediction API is running"
    }


def test_predict():
    data = {
        "area_sqft": 1800,
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "parking": 1
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 200

    result = response.json()

    assert "predicted_price" in result
    assert isinstance(result["predicted_price"], float)
    assert result["predicted_price"] > 0


def test_predict_invalid_data():
    data = {
        "area_sqft": "invalid",
        "bedrooms": 3,
        "bathrooms": 2,
        "stories": 2,
        "parking": 1
    }

    response = client.post("/predict", json=data)

    assert response.status_code == 422