from fastapi import APIRouter, HTTPException
from typing import List

from app.services.utils import fetch_and_process_files_metadata

router = APIRouter()

@router.get("/files/metadata", response_model=List[dict])
async def get_files_metadata():
    """
    Endpoint to fetch files from the predefined GitHub repository and return their metadata as JSON.

    Returns:
        JSON list of file metadata.
    """
    try:
        files_metadata = await fetch_and_process_files_metadata()
        return files_metadata
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))