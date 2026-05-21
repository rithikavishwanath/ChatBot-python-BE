import email
from os import name

from sqlalchemy import Column, Integer, String, Boolean, true
from app.core.database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key= True, index= True)
  name = Column(String, nullable= False)
  email = Column(String, nullable= False, unique= True)
  password = Column(String, nullable= False)
  is_active = Column(Boolean, default= True)
