import hashlib

from models.User import User
from models.db.db_conection import get_session
from controllers.UserController import UserController
from sqlmodel import Session
from customtkinter import *


class RegistrationView:
    is_login: bool = None
    ctrl_user: UserController = UserController()
    session: Session = get_session()
    box_email: CTkEntry
    box_pass: CTkEntry
    btn_login: CTkButton
    error_txt: str = ""

    def __init__(self, app_: CTk):
        super().__init__()

    @classmethod
    def give_frame(cls, app_) -> CTkFrame:
        pass

    @classmethod
    def create_user(cls):
        u = User()
        cls.ctrl_user.add(u, cls.session)
