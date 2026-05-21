from dotenv import load_dotenv
import os

load_dotenv()

# class Setting:
#   DATABASE_URL = os.getenv("DATABASE_URL")
#   SECRET_KEY = os.getenv("SECRET_KEY")

class Setting:
  DATABASE_URL : str
  SECRET_KEY : str

  def __init__(self):
    database_url = os.getenv("DATABASE_URL")
    secret_key = os.getenv("SECRET_KEY")

    if not database_url:
      raise ValueError("database url is missing")
    
    if not secret_key:
      return ValueError("secret key is missing")
    
    self.DATABASE_URL = database_url
    self.SECRET_KEY = secret_key

setting = Setting()