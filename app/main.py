# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as student_router

app = FastAPI(title="Mark Registry Web API")

"""connect router to main app instance"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allowing all dev versions
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router, prefix="/api")
