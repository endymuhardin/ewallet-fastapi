from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

from app.main import app
from app.models.customer import Customer
from app.database import get_db

client = TestClient(app)

# Mock data untuk customer
mock_customer_data = Customer(id="123", name="Test Customer", email="test@example.com")

def test_get_customer_by_id():
    # Membuat mock session dan query
    mock_db = MagicMock(spec=Session)
    
    # Mengatur return value ketika filter dipanggil
    mock_db.query().filter().first.return_value = mock_customer_data
    
    # Mengatur dependensi get_db agar mengembalikan mock_db
    app.dependency_overrides[get_db] = lambda: mock_db
    
    # Melakukan request ke endpoint
    response = client.get("/customer/123")
    
    # Mengembalikan kembali dependensi setelah test
    app.dependency_overrides = {}
    
    # Assert bahwa status code adalah 200
    assert response.status_code == 200
    
    # Assert bahwa data yang dikembalikan sesuai dengan mock data
    expected_response = {
        "id": "123",
        "name": "Test Customer",
        "email": "test@example.com"
    }
    assert response.json() == expected_response
