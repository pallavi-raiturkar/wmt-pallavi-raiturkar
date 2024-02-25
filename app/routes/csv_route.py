from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import csv
import os
from tempfile import NamedTemporaryFile
import logging

from app.services.utils import fetch_and_process_files_metadata

router = APIRouter()
logger = logging.getLogger("file_metadata_app")

@router.get("/files/metadata/csv")
async def get_files_metadata_csv():
    """
    Endpoint to fetch files from the predefined GitHub repository, generate a CSV with their metadata,
    and return it as a downloadable file.

    Returns:
        FileResponse: A CSV file containing the metadata of each file.
    """
    logger.info("CSV endpoint triggered")
    global temp_file
    try:
        files_metadata = await fetch_and_process_files_metadata()

        # Create a temporary file to store the CSV data
        temp_file = NamedTemporaryFile(mode="w+", delete=False, suffix=".csv", newline='', encoding='utf-8')
        fieldnames = ['filename', 'sha256', 'size', 'word_count', 'unique_words', 'date']

        # Write metadata to the CSV file
        with temp_file as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for file_metadata in files_metadata:
                writer.writerow(file_metadata)

        # Return the CSV file as a downloadable response
        return FileResponse(path=temp_file.name, filename="interview.csv", media_type='text/csv')
    except Exception as e:
        # Ensure temporary file is cleaned up in case of an error
        os.unlink(temp_file.name)
        raise HTTPException(status_code=500, detail=str(e))