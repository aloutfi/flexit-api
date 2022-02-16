from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_the_app():
    response = client.get("/health_check")
    assert response.status_code == 200
