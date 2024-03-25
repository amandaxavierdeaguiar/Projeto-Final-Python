import hashlib
import tkinter as tk
from pathlib import Path
from tkinter import *
from tkinter import PhotoImage
from tkinter.ttk import Label

import ttkbootstrap as ttk
from pydantic import ValidationError
from ttkbootstrap.constants import *

from models.UserAuthentication import UserAuthentication
from views.MainView import MainView

PATH = Path(__file__).parent / "assets"


class LoginView(ttk.Frame):
    user: UserAuthentication
    login_entry_var: ttk.StringVar
    password_entry_var: ttk.StringVar
    login_entry: Entry
    password_entry: Entry
    login_frame: ttk.Frame
    img: PhotoImage
    img_lbl: Label

    def __init__(self, master):
        self.root = master
        super().__init__(master, padding=(10, 5))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.login_entry_var = ttk.StringVar(value="")
        self.password_entry_var = ttk.StringVar(value="")

        self.login_frame = self.create_frame()

        # form entries
        self.create_form_entry("Login", self.login_entry_var)
        self.create_form_entry("Password", self.password_entry_var)
        self.create_buttonbox()

    def create_frame(self):
        self.login_frame = Frame(
            self, width=600, height=400, pady=50, padx=50, background="white"
        )
        # self.login_frame.configure(padding=50)
        self.login_frame.pack(expand=False)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.img = PhotoImage(master=self.login_frame, file=PATH / "login.png")
        self.img_lbl = Label(master=self.login_frame, image=self.img)
        self.img_lbl.configure(
            background="white",
            compound="image",
            anchor="center",
            justify="center",
            padding=5,
        )
        self.img_lbl.pack(side=TOP, padx=5, pady=5, fill=tk.X, expand=tk.YES)

        return self.login_frame

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = Frame(master=self.login_frame)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = Label(master=container, text=label.title(), width=10)
        lbl.configure(background="white", justify="right", anchor="e")
        lbl.pack(side=LEFT, padx=5)

        if label.title() == "Password":
            self.password_entry = Entry(
                master=container, textvariable=variable, show="*"
            )
            self.password_entry.pack(side=LEFT, padx=5, fill=X, expand=YES)
        else:
            self.login_entry = Entry(master=container, textvariable=variable)
            self.login_entry.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = Frame(self.login_frame)
        container.pack(fill=tk.BOTH, expand=YES, side="bottom", pady=5)

        sub_btn = Button(
            master=container,
            text="Login",
            cursor="hand2",
            command=self.on_submit,
            width=15,
        )
        sub_btn.pack(fill=tk.BOTH, padx=5, pady=5)
        sub_btn.focus_set()

        cnl_btn = Button(
            master=container,
            text="Registar",
            cursor="hand2",
            command=self.on_cancel,
            width=15,
        )
        cnl_btn.pack(fill=tk.BOTH, padx=5, pady=5)

    def on_submit(self):
        try:
            email = self.login_entry.get()
            password = self.hash_password(self.password_entry.get())
            self.user = UserAuthentication()
            self.user.check(email, password)
            if self.user.is_login:
                self.destroy()
                self.wait_window(MainView(self.root, self.user))
                # MainView(self.root, self.user)
        except ValidationError as e:
            print(e)

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()

    @classmethod
    def hash_password(cls, pwd):
        """Hash a password using SHA-256 algorithm"""
        pwd_bytes = pwd.encode("utf-8")
        hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
        return hashed_pwd
