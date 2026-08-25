from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine
from app.routers.employee import emp_router as employee_router
from app.routers.department import dep_router as department_router
from app.models.employee import Employee
from app.models.department import Department


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


app.include_router(employee_router)
app.include_router(department_router)

@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }