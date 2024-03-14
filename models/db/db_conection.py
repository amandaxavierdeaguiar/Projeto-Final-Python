from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv
#import psycopg2

load_dotenv()

# sqlite_file_name = "database.db"
url = str(os.getenv('SECRET_BD'))
sqlite_url = f"{url}"

def engine():
    return create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine())

"""sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)"""    