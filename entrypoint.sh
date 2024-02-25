#!/bin/bash

# Start Uvicorn in the background
uvicorn app.main:app --host 0.0.0.0 --port 80 &

# Wait for the server to launch
echo "Waiting for server to launch on port 80..."
while ! nc -z localhost 80; do
  sleep 0.1
done
echo "Server launched"

# Call the CSV endpoint and download the file
echo "Downloading CSV file from the endpoint..."
curl http://localhost:80/files/metadata/csv --output interview.csv

# Keep the container running after the download
echo "Download complete. Server is still running."
wait