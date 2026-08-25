from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
)
from app.services.employee_services import EmployeeService


emp_router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


employee_service = EmployeeService()

@emp_router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(employee_data: EmployeeCreate, db: Session = Depends(get_db)):

    return employee_service.create_employee(
        db,
        employee_data
    )


@emp_router.get(
    "",
    response_model=list[EmployeeResponse]
)
def get_all_employees(db: Session = Depends(get_db)):

    return employee_service.get_all_employees(db)


@emp_router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    return employee_service.get_employee(
        db,
        employee_id
    )


@emp_router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):

    return employee_service.update_employee(
        db,
        employee_id,
        employee_data
    )


@emp_router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee_service.delete_employee(
        db,
        employee_id
    )