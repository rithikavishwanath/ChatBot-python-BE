from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
  name : str
  email : EmailStr
  password : str


class UserResponse(BaseModel):
  id : int
  name : int
  email : str
  is_active : bool

  class Config:
    from_attributes = True