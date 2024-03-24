import tkinter as tk
from pathlib import Path
from tkinter import *

import ttkbootstrap as ttk
from PIL import Image, ImageTk

PATH = Path(__file__).parent / "assets"


class DescriptionProduct:
    root = ttk.Window(themename="cosmo")

    def __init__(self):
        super().__init__()

        self.window_description()
        self.frame_photo_description()
        self.entrys_product()

        # form entries
        self.name = ttk.StringVar(value="")
        self.bar_cod = ttk.StringVar(value="")
        self.description = ttk.StringVar(value="")
        self.price = ttk.DoubleVar(value="")
        self.category = ttk.StringVar(value="")
        self.brand = ttk.StringVar(value="")

        self.create_form_products("name", self.name)  # get
        self.create_form_products("bar_cod", self.bar_cod)
        # self.create_form_products("description", self.description)
        self.create_form_products("price", self.price)
        self.create_form_products("category", self.category)
        self.create_form_products("brand", self.brand)

        self.textbox_description_prod()
        self.create_buttonbox()
        # self.root.configure(background='blue')
        self.root.mainloop()

    @classmethod
    def window_description(cls):
        cls.root.title("Descrição do Produto")
        cls.root.geometry("1000x650")
        cls.root.minsize(width=756, height=545)

    @classmethod
    def frame_photo_description(cls):
        # Frame para dividir a tela.
        prod_frame_description = ttk.Frame(cls.root, width=300, height=1000)
        prod_frame_description.pack(fill=tk.Y, side=LEFT)

        style = ttk.Style()
        style.configure(
            "Custom.TFrame",
            background=style.colors.primary,
        )

        prod_frame_description.config(
            style="Custom.TFrame",
        )

        img_logo = Image.open(PATH / "alho_frances.png")
        cls.img_logo = ImageTk.PhotoImage(img_logo.resize((250, 250)))
        cls.button1 = Label(
            prod_frame_description, width=250, height=250, image=cls.img_logo, text=""
        ).place(relx=0.08, rely=0.3)

        return prod_frame_description

    @classmethod
    def entrys_product(cls):
        register_prod = ttk.Frame(cls.root, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)
        # Colocando cor na frame

        # form header
        hdr_txt = "Digite os dados do produto:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        style = ttk.Style()
        style.configure(
            "Custom.TLabel",
            foreground=style.colors.primary,
        )
        hdr.config(
            style="Custom.TLabel",
        )

        hdr.pack(pady=20)

    @classmethod
    def create_form_products(cls, label, variable):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = Entry(
            master=container,
            textvariable=variable,
            bg="white",
            relief="solid",
            borderwidth=0.5,
            state=DISABLED,
        )
        # ent.pack(padx=5, pady=5)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    @classmethod
    def create_buttonbox(cls):
        """Caixa Botoes App"""
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=cls.on_submit,
            bootstyle="SUCCESS",
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=cls.on_cancel,
            bootstyle="DANGER",
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    # inclui
    @classmethod
    def textbox_description_prod(cls):
        container = ttk.Frame(cls.root)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text="Descrição:", width=10)
        lbl.pack(side=LEFT, padx=5)

        ent_description = ttk.ScrolledText(
            master=container,
            wrap=WORD,
            height=5,
            state=DISABLED,
            relief="solid",
            borderwidth=3,
        )
        ent_description.pack(side=LEFT, padx=5, fill=X, expand=YES)

    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        print("Nome:", cls.name.get())
        print("Codigo Barras:", cls.bar_cod.get())
        print("Descrição:", cls.description.get())
        print("Preço:", cls.price.get())
        print("Categoria:", cls.category.get())
        print("Marca:", cls.brand.get())
        return (
            cls.bar_cod.get(),
            cls.name.get(),
            cls.description.get(),
            cls.price.get(),
            cls.category.get(),
            cls.brand.get(),
        )

    @classmethod
    def on_cancel(self):
        # Cancela e sai da app
        self.quit()


if __name__ == "__main__":
    inicio = DescriptionProduct()
    # Test code

    inicio.root.mainloop()
