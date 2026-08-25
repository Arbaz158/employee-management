from app.db.base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

