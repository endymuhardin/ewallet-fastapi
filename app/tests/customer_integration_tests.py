
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_customer_by_id():
    response = client.get("/customer/c001")
    assert response.status_code == 200
    assert response.json() == {"id": "c001", "name": "Customer 001", "email" : "c001@yopmail.com"}