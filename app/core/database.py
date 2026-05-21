from math import fabs

from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import setting

engine = create_engine(setting.DATABASE_URL)

SessionLocal = sessionmaker(
  autoflush= False,
  bind= engine
)

Base = declarative_base()