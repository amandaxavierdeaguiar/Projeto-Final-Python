import tkinter as tk
from tkinter import *
from tkinter import ttk

import ttkbootstrap
from PIL import Image, ImageTk
from sqlmodel import Session
from ttkbootstrap import Style
from tkinter.ttk import Label
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview

from controllers.StockController import StockController
from models.db.db_conection import get_session


class Inicio:
    ctrl_stock: StockController = StockController()
    session: Session = get_session()
    frame_back: tk.Frame
    main_frame: tk.Frame
    login_frame: tk.Frame
    photo_image: PhotoImage
    theme: Style
    image: Image
    img: Label
    root: tk = Tk()

    def __init__(self):
        super().__init__()
        # colocar o menu
        self.window()
        self.root.mainloop()

    @classmethod
    def window(cls):
        cls.root.title("Stock Management")
        cls.root.geometry("750x750")
        cls.root.resizable(width=True, height=True)
        cls.root.style = Style(theme="cosmo")
        cls.root.configure(background="#EBEBEB")

        cls.main_frame = cls.create_frame()

    @classmethod
    def create_frame(cls) -> Frame:
        login_frame = tk.Frame(
            cls.root,
            width=600,
            height=400,
        )
        login_frame.configure(background="white", padx=50, pady=50)
        login_frame.pack(fill=tk.NONE, side="bottom", expand=True)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        cls.photo_image = PhotoImage("./assets/login.png")

        image = Image.open("assets/login.png")
        image = image.resize((130, 130), None)
        cls.photo_image = ImageTk.PhotoImage(image)
        img = Label(login_frame, image=cls.photo_image)
        img.pack(pady=20)
        # Botão Inserir dados Login
        label_user = Label(
            login_frame,
            text="Digite seu nome de usuário:",
            font=("Arial", 10),
            bootstyle="info",
        )
        label_user.pack()

        entrada_usuario = ttk.Entry(login_frame, width=30, bootstyle="primary")
        entrada_usuario.pack(pady=10)

        label_senha = Label(
            login_frame,
            text="Digite sua senha:",
            font=("Arial", 10),
            bootstyle="info",
        )
        label_senha.pack()

        entrada_senha = ttk.Entry(login_frame, show="*", width=30, bootstyle="primary")
        entrada_senha.pack(pady=10)

        botao_entrar = ttk.Button(
            login_frame, text="Entrar", bootstyle=("DEFAULT"), cursor="hand2", width=30
        )  # command=self.realizar_login
        botao_entrar.pack(pady=10)
        botao_registar = ttk.Button(
            login_frame, text="Registar", style="Secondary", cursor="hand2", width=30
        )  # command=self.realizar_login
        botao_registar.pack(pady=10)


if __name__ == "__main__":
    Inicio()
