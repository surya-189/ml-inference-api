from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction():
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5, 1.4, 0.2]}
    )

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "confidence" in result


def test_invalid_input():
    response = client.post(
        "/predict",
        json={"features": [5.1, 3.5]}
    )

    assert response.status_code == 422