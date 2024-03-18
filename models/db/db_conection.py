import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session

load_dotenv()

# sqlite_file_name = "database.db"
# url = str(os.getenv('SECRET_BD'))
# url = str(os.getenv('SECRET_BD2'))
DB_USER = str(os.getenv('DB_USER'))
DB_PASS = str(os.getenv('DB_PASS'))
DB_HOST = str(os.getenv('DB_HOST'))
DB_NAME = str(os.getenv('DB_NAME'))
url = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'


def get_engine():
    return create_engine(url, echo=True)


# def get_engine_2():
#    return create_engine(url2, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(get_engine())


def get_session():
    return Session(get_engine())
