from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import health, profile

app = FastAPI(title="logbook-be")

# CORS (dev: 전체 허용 / prod: 도메인 제한)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # prod에선 프론트 도메인으로 제한
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(profile.router)