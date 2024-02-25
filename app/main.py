from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health_route import router as health_router
from app.routes.json_route import router as json_router
from app.routes.csv_route import router as csv_router
from app.logging_config import setup_logging

# Configure logging
setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Specify domains for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(json_router)
app.include_router(health_router)
app.include_router(csv_router)
