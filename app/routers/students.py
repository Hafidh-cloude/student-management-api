"""
    === Student Router Module ===

Menyediakan endpoint REST API untuk CRUD
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import StudentCreate, StudentResponse, StudentUpdate
from app.database import get_db
from app.models import Student

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


# Retrieve all student record
@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# Create new student record
@router.post("/", response_model=StudentResponse)
def create_student(
    student_data: StudentCreate,
    db: Session = Depends(get_db),
):
    student = Student(
        name=student_data.name,
        major=student_data.major,
        semester=student_data.semester,
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


# Retrieve student by ID
@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found!",
        )
    return student


# Update exsisting student
@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found!",
        )

    student.name = student_data.name
    student.major = student_data.major
    student.semester = student_data.semester

    db.commit()
    db.refresh(student)

    return student


# Delete exsisting student
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found!",
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully",
    }
