from pathlib import Path
from tkinter import *
from tkinter import filedialog

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from sqlmodel import Session

from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.Base.BaseWindow import BaseWindow
from models.Enums.TypeAccess import TypeAccess

PATH = Path(__file__).parent.parent / "assets"


class UserView(ttk.Frame):
    root: BaseWindow
    session: Session = get_session()  # <-
    user: UserAuthentication
    main_frame: ttk.Frame
    side_frame: ttk.Frame
    img_user: ImageTk.PhotoImage
    button_img: Label
    # nome
    name: StringVar
    name_ent: Entry
    # login
    login: StringVar
    login_ent: Entry
    # password
    password: StringVar
    password_ent: Entry
    # type_access
    type_access: IntVar
    type_access_ent: ttk.Combobox

    def __init__(self, master_, user_login, user_select=None):
        super().__init__(master_, padding=(10, 5))
        self.root = master_

        self.main_frame, self.side_frame = self.get_frames(self.root)
        self.title_main_frame(self.main_frame)

        # form entries
        self.name = ttk.StringVar(value="")
        self.login = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
        self.password_confirm = ttk.StringVar(value="")
        self.typeAcess = ttk.IntVar(value=None)

        self.name_ent = self.create_form_user(self.main_frame, "Nome:", self.name.get())
        self.login_ent = self.create_form_user(self.main_frame, "Login:", self.login.get())

        self.password_ent = self.create_form_user(self.main_frame, "Password:", self.password.get())
        self.password_confirm_ent = self.password_entry(self.main_frame)

        self.combobox_type_user(self.main_frame)
        self.create_buttonbox(self.main_frame)
        # self.root.configure(background='blue')

    @classmethod
    def get_frames(cls, master_):
        # Frame para dividir a tela.
        side_frame = ttk.Frame(master_, width=300, height=1000)
        side_frame.pack(fill=Y, side=LEFT)

        cls.main_frame = ttk.Frame(master_, width=300, height=1000)
        cls.main_frame.pack(fill=Y, side=LEFT)

        # style = ttk.Style()
        # style.configure("Custom.TFrame", background=style.colors.primary, )

        # cls.main_frame.config(style="Custom.TFrame", )

        img_user = Image.open(PATH / "icons/insert_user_bg2.png")
        cls.img_user = ImageTk.PhotoImage(img_user.resize((350, 350)))
        cls.button_img = Label(
                master=side_frame,
                width=250,
                height=250,
                image=cls.img_user,
                text="",
                borderwidth=0,
                highlightthickness=0,
                bd=0
        )
        cls.button_img.place(relx=.08, rely=.3)
        return cls.main_frame

    @classmethod
    def title_main_frame(cls, main_frame):
        register_prod = ttk.Frame(main_frame, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)
        # Colocando cor na frame

        # form header
        hdr_txt = "Digite os dados do User:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        style = ttk.Style()
        style.configure("Custom.TLabel", foreground=style.colors.primary, )
        hdr.config(style="Custom.TLabel", )

        hdr.pack(pady=20)

    @classmethod
    def create_form_user(cls, main_frame, label, variable):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(main_frame)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=13)
        lbl.pack(side=LEFT, padx=5)

        ent = Entry(master=container, textvariable=variable, bg="white", relief="solid", borderwidth=0.5)

        ent.pack(side=LEFT, padx=20, fill=X, expand=YES)

        return ent

    @classmethod
    def create_buttonbox(cls, main_frame):
        """Caixa Botoes App"""
        container = ttk.Frame(main_frame)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
                master=container,
                text="Submit",
                command=cls.on_submit,
                bootstyle='SUCCESS',
                width=6,
        )
        sub_btn.pack(side=RIGHT, padx=20)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
                master=container,
                text="Cancel",
                command=cls.on_cancel,
                bootstyle='DANGER',
                width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    """ Colocar a senha """

    @classmethod
    def password_entry(cls, main_frame):
        frame_password = ttk.Frame(main_frame)
        frame_password.pack(fill=X, expand=YES, pady=5)

        lbl_password = ttk.Label(frame_password, text="Password", width=13)
        lbl_password.pack(side=LEFT, padx=5)

        password_entry_ = ttk.Entry(frame_password, show="*")
        password_entry_.pack(side=LEFT, padx=20, fill=X, expand=YES)

        lbl_password_repeat = ttk.Label(frame_password, text="Digite novamente:", width=16)
        lbl_password_repeat.pack(side=LEFT, padx=5)

        repeat_password_entry = ttk.Entry(frame_password)
        repeat_password_entry.pack(side=LEFT, padx=20, fill=X, expand=YES)
        return repeat_password_entry

    @classmethod
    def combobox_type_user(cls, main_frame):
        frame_combobox = ttk.Frame(main_frame)
        frame_combobox.pack(fill=X, expand=YES, pady=5)

        lbl_combobox = ttk.Label(frame_combobox, text="Tipo de Acesso", width=13)
        lbl_combobox.pack(side=LEFT, padx=5)

        type_acess = ttk.Combobox(frame_combobox, state="readonly", values=TypeAccess.return_types())
        type_acess.current(0)
        type_acess.pack(side=LEFT, padx=20, fill=X, expand=YES)

        return type_acess

    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name.get())
        print("Login:", cls.login.get())
        print("Password:", cls.password.get())
        print("Tipo de Acesso:", cls.type_access.get())

        return cls.name.get(), cls.login.get(), cls.password.get(), cls.type_access.get()

    @classmethod
    def on_cancel(cls):
        # Cancela e sai da app
        cls.quit()
