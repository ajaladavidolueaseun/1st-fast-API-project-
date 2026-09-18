from pydantic import BaseModel, EmailStr

class LecturerBase(BaseModel):
    name: str
    department: str
    email: EmailStr

class LecturerCreate(LecturerBase):
    pass

class LecturerResponse(LecturerBase):
    id: int

    class Config:
        from_attributes = True