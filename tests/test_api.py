"""
test cases for app
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    """
    test api is running or not
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "you have successfully lauched the app"}


def test_predict():
    """
    test if predicted output is correct
    """
    response = client.post("/predict/", data={"text": "Skilled in pandas and ML"})
    assert response.status_code == 200
    assert "prediction" in response.json()
