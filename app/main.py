"""
    === Application Entry Point ===

Inisialisasi database dan FastAPI
"""

from fastapi import FastAPI

from app.database import Base, engine
from app.routers.students import router as student_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="REST API for managing student data.",
    version="1.0.0",
)

app.include_router(student_router)
