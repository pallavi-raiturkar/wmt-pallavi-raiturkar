from fastapi import APIRouter
import logging

router = APIRouter()

logger = logging.getLogger("file_metadata_app")
@router.get("/health")
def health_check():
    logger.info("Health endpoint triggered")
    return {"status": "healthy"}