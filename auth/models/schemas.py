from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int


class User(UserBase):
    email: EmailStr
    hashed_password: str
    


