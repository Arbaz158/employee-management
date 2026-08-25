from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.department import DepartmentResponse, DepartmentCreate
from app.services.department_service import DepartmentService
from app.db.database import get_db


dep_router = APIRouter(
    prefix="/api/v1/department",
    tags=["Departments"]
)

department_service = DepartmentService()

@dep_router.post("", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
def create_department(department_data: DepartmentCreate, db: Session = Depends(get_db)):
    return department_service.create_department(
        db,
        department_data
    )
