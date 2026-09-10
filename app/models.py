"""
    === Database Models ===

Mendefinisikan model database untuk data mahasiswa.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    major: Mapped[str] = mapped_column(String(100), nullable=False)
    semester: Mapped[int] = mapped_column(nullable=False)
