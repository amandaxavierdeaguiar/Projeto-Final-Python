from models.db.db_conection import get_session
from sqlmodel import Session
from customtkinter import *
from CTkTable import CTkTable


class StockView:
    app: CTk
    session: Session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def give_frame(cls) -> CTkFrame:
        frame = CTkFrame()
        return frame