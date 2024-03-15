import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, MetaData

load_dotenv()

# sqlite_file_name = "database.db"
url = str(os.getenv('SECRET_BD'))
sqlite_url = f"{url}"


def engine():
    return create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine())
