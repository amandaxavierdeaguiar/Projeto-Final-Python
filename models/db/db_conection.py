import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

# sqlite_file_name = "database.db"
# url = str(os.getenv('SECRET_BD'))
sqlite_url = str(os.getenv('SECRET_BD2'))


def get_engine():
    return create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())


def get_session():
    return Session(get_engine())
