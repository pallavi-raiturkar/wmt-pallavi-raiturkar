from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.routes.health_route import router as health_router
from app.routes.json_route import router as json_router
from app.routes.csv_route import router as csv_router

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


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=80)