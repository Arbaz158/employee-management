from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: int


class EmployeeUpdate(BaseModel):
    name: str
    email: EmailStr
    department: str
    salary: int


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    salary: int

    model_config = {
        "from_attributes": True
    }