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
    You might need to mock the actual downloading and processing functions
    if they rely on external resources or have a significant execution time.
    """
    response = client.get("/files/metadata")
    assert response.status_code == 200
    # Assert based on the expected JSON structure
    # Example:
    # assert response.json() == [{"filename": "example.txt", "size": 123, ...}]

def test_files_metadata_csv():
    """
    Test the endpoint that returns file metadata as a downloadable CSV file.
    This test should check for the response headers and content type to ensure
    it's a CSV file being returned.
    """
    response = client.get("/files/metadata/csv")
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('text/csv')
    # You might also want to check the content-disposition header or the body of the response
    # to ensure it matches the expected CSV format.