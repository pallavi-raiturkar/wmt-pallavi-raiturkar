from fastapi.testclient import TestClient
from app.main import app  # Adjust the import path based on your project structure

client = TestClient(app)

def test_health_check():
    """
    Test the health check endpoint to ensure it returns a 200 status code
    and the expected response body.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_files_metadata_json():
    """
    Test the endpoint that returns file metadata in JSON format.
    """
    response = client.get("/files/metadata")
    assert response.status_code == 200

def test_files_metadata_csv():
    """
    Test the endpoint that returns file metadata as a downloadable CSV file.
    """
    response = client.get("/files/metadata/csv")
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('text/csv')