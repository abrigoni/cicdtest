from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    """
        tests the health checkpoint's status and body
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
