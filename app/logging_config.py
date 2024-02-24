import logging
import sys

def setup_logging():
    LOGGING_FORMAT = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
    LOGGING_LEVEL = logging.INFO

    logging.basicConfig(
        level=LOGGING_LEVEL,
        format=LOGGING_FORMAT,
        handlers=[
            logging.StreamHandler(sys.stdout)  # Ensure logs are printed to stdout
            # Consider adding file handlers for production use
        ]
    )

    # Example of configuring a specific logger for a module
    logger = logging.getLogger("file_metadata_app")
    logger.setLevel(LOGGING_LEVEL)

    # Suppress overly verbose logs from libraries that you don't control
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("aiohttp").setLevel(logging.WARNING)