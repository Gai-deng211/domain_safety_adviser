from fastapi.testclient import TestClient
from app.schemas import RegistrationData
import pytest

from main import app

client = TestClient(app)

@pytest.fixture
def home():
    response = client.get("/")
    return {
        "status_code": response.status_code,
        "message": response.json()["message"]
    }

@pytest.fixture
def valid_url_lookup():
    valid_response = client.get("/api/url_lookup?domain_url=bcit.ca")
    return valid_response
    
@pytest.fixture
def invalid_url_lookup():
    invalid_response = client.get("/api/url_lookup?domain_url=ssdgai")
    return invalid_response

class Test_Api_Endpoints:
    def test_home(self, home):
        assert home["status_code"] == 200
        assert home["message"] == "main application is running ✅🚀🚀🚀"
    
    def test_valid_url(self, valid_url_lookup):
        assert valid_url_lookup.status_code == 200
        assert valid_url_lookup.json()["domain"] == "bcit.ca"
        
        # Test conversion to pydantic model
        model = RegistrationData(**valid_url_lookup.json())
        assert model.domain == "bcit.ca"
    
    def test_invalid_url(self, invalid_url_lookup):
        assert invalid_url_lookup.status_code == 400
        assert "detail" in invalid_url_lookup.json()
        assert invalid_url_lookup.json()["detail"] == "Invalid URL!"