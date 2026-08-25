from sqlalchemy.orm import Session

from app.repositories.department_repository import DepartmentRepository
from app.schemas.department import DepartmentCreate
from app.models.department import Department


class DepartmentService:

    def __init__(self):
        self.repository = DepartmentRepository()

    def create_department(
        self,
        db: Session,
        department_data: DepartmentCreate
    ) -> Department:
        return self.repository.create(db, department_data)