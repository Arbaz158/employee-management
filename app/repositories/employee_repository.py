from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:

    def create(
        self,
        db: Session,
        employee_data: EmployeeCreate
    ) -> Employee:

        employee = Employee(
            name=employee_data.name,
            email=employee_data.email,
            department=employee_data.department,
            salary=employee_data.salary,
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    def get_all(
        self,
        db: Session
    ) -> list[Employee]:

        return db.query(Employee).all()

    def get_by_id(
        self,
        db: Session,
        employee_id: int
    ) -> Employee | None:

        return (
            db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> Employee | None:

        return (
            db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    def update(
        self,
        db: Session,
        employee: Employee,
        employee_data: EmployeeUpdate
    ) -> Employee:

        employee.name = employee_data.name
        employee.email = employee_data.email
        employee.department = employee_data.department
        employee.salary = employee_data.salary

        db.commit()
        db.refresh(employee)

        return employee

    def delete(
        self,
        db: Session,
        employee: Employee
    ) -> None:

        db.delete(employee)
        db.commit()