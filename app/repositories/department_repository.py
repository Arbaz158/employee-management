from sqlalchemy.orm import Session

from app.models import department
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate


class DepartmentRepository:

    def create(self, db: Session, department_data: DepartmentCreate) -> Department:
        department = Department(
            name=department_data.name,
        )
        db.add(department)
        db.commit()
        db.refresh(department)
        return department


    def update(self, db: Session, department: Department ,department_data: DepartmentUpdate) -> Department:
        department.name = department_data.name
        db.commit()
        return department