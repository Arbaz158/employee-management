from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeService:

    def __init__(self):
        self.repository = EmployeeRepository()

    def create_employee(
        self,
        db: Session,
        employee_data: EmployeeCreate
    ):

        existing_employee = self.repository.get_by_email(
            db,
            employee_data.email
        )

        if existing_employee:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Employee with this email already exists"
            )

        return self.repository.create(
            db,
            employee_data
        )

    def get_all_employees(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    def get_employee(
        self,
        db: Session,
        employee_id: int
    ):

        employee = self.repository.get_by_id(
            db,
            employee_id
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        return employee

    def update_employee(
        self,
        db: Session,
        employee_id: int,
        employee_data: EmployeeUpdate
    ):

        employee = self.repository.get_by_id(
            db,
            employee_id
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        existing_employee = self.repository.get_by_email(
            db,
            employee_data.email
        )

        if (
            existing_employee
            and existing_employee.id != employee_id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already belongs to another employee"
            )

        return self.repository.update(
            db,
            employee,
            employee_data
        )

    def delete_employee(
        self,
        db: Session,
        employee_id: int
    ):

        employee = self.repository.get_by_id(
            db,
            employee_id
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        self.repository.delete(db, employee)