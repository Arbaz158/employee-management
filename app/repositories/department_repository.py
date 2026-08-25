from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate


class DepartmentRepository:

    def create(self, db: Session, department_data: DepartmentCreate) -> Department:
        department = Department(
            name=department_data.name,
        )
        db.add(department)
        db.commit()
        db.refresh(department)
        return department


