from fastapi import FastAPI

from app.api.routes import router as student_router

app = FastAPI(title="Mark Registry Web API")

"""connect router to main app instance"""
app.include_router(student_router)
