"""
    === Schemas ===

Validasi data dan response API.
"""

from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    major: str = Field(min_length=1, max_length=100)
    semester: int = Field(ge=1, le=14)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    major: str = Field(min_length=1, max_length=100)
    semester: int = Field(ge=1, le=14)


class StudentResponse(BaseModel):
    id: int
    name: str
    major: str
    semester: int

    model_config = {"from_attributes": True}
