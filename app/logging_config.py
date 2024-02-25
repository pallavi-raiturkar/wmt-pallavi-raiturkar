import logging
import sys

def setup_logging():
    LOGGING_FORMAT = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
    LOGGING_LEVEL = logging.INFO

    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Generic logger
    logger = logging.getLogger("file_metadata_app")
    logger.setLevel(LOGGING_LEVEL)

    # Suppress overly verbose logs
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)