from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Employee(Base):

    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    salary: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )