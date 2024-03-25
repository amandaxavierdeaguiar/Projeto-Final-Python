from pathlib import Path
from tkinter import *
from tkinter import filedialog

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from sqlmodel import Session

from controllers.BrandController import BrandController
from controllers.CategoryController import CategoryController
from controllers.ProductController import ProductController
from models.Product import Product
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from views.Base.BaseWindow import BaseWindow

PATH = Path(__file__).parent.parent / "assets"


class RegistrationProduct:
    root: BaseWindow
    ctrl_brand: BrandController = BrandController()  # <-
    ctrl_category: CategoryController = CategoryController()  # <-
    ctrl_product: ProductController = ProductController()  # <-
    session: Session = get_session()  # <-
    user: UserAuthentication
    file_name: str = ""
    main_frame: ttk.Frame
    side_frame: ttk.Frame
    # nome
    name: StringVar
    # Imagem Produto
    img_product: ImageTk.PhotoImage
    img_product_lbl: Label
    # bar code
    bar_cod: ttk.IntVar
    # description
    description: ttk.StringVar
    # price
    price: ttk.DoubleVar
    # category
    category: ttk.StringVar
    # Brand
    brand: ttk.StringVar

    def __init__(self, user_, product_select=None):
        super().__init__()
        self.root = BaseWindow(
            title="Inserir Produto",
            iconphoto=f"{PATH}/icons/logo-stock.png",
            themename="cosmo",
            background="#EBEBEB",
            resizable=(True, True),
            size=[1000, 650],
            minsize=[756, 545],
        )
        self.user = user_
        photo_temp = (
            None
            if product_select is None or product_select["Foto"] == ""
            else product_select["Foto"]
        )
        self.main_frame, self.side_frame = self.frame_photo_product(photo_temp)
        self.title_frame()

        # nome
        name_temp = "" if product_select is None else product_select["Produto"]
        self.name: StringVar = ttk.StringVar(value=name_temp)
        # description
        description_temp = "" if product_select is None else product_select["Descrição"]
        self.description: ttk.StringVar = ttk.StringVar(value=description_temp)
        # price
        price_temp = "" if product_select is None else product_select["Preço"]
        self.price: ttk.DoubleVar = ttk.DoubleVar(value=float(price_temp))
        # category
        category_temp = "" if product_select is None else product_select["Categoria"]
        self.category: ttk.StringVar = ttk.StringVar(value=category_temp)
        # Brand
        brand_temp = "" if product_select is None else product_select["Marca"]
        self.brand: ttk.StringVar = ttk.StringVar(value=brand_temp)

        self.name_ent = self.create_form_entry("Nome", self.name, "text")
        self.price_ent = self.create_form_entry("Preço", self.price, "double")
        self.category_ent = self.create_combobox(
            "Categoria:", self.ctrl_category.get_all(self.session), self.category
        )
        self.brand_ent = self.create_combobox(
            "Marca:", self.ctrl_brand.get_all(self.session), self.brand
        )
        self.description_ent = self.textbox_description()
        self.create_buttonbox()
        self.root.mainloop()

    def frame_photo_product(self, image_path):
        style = ttk.Style()
        style.configure("Custom.TFrame", background=style.colors.primary)
        style.configure(
            "Custom.Button",
            background=style.colors.info,
        )
        # Frame para dividir a tela.
        img_frame = ttk.Frame(
            self.root, width=300, height=1000, style=style.colors.primary
        )

        img_frame.pack(fill=Y, side=LEFT)
        if image_path is None:
            button_insert_img = Button(
                img_frame,
                text="ADICIONE A IMAGEM",
                cursor="hand2",
                command=self.on_select_image,  # Acrescentei
            )
            button_insert_img.place(relx=0.2, rely=0.6)
        else:
            img_path_temp = Image.open(PATH / "icons/logo-stock-b.png")
            self.img_product = ImageTk.PhotoImage(img_path_temp.resize((250, 250)))
            self.img_product_lbl = Label(
                img_frame,
                width=250,
                height=250,
                image=self.img_product,
                text="",
                pady=40,
            )
            self.img_product_lbl.place(relx=0.07, rely=0.1)
        prod_frame = ttk.Frame(self.root, width=300, height=1000, padding=60)
        prod_frame.pack(fill=BOTH, side=LEFT)
        return prod_frame, img_frame

    def title_frame(self):
        register_prod = ttk.Frame(self.main_frame, padding=(20, 10))
        register_prod.pack(fill=BOTH, expand=YES)

        # form header
        hdr_txt = "Digite os dados do produto:"
        hdr = ttk.Label(register_prod, text=hdr_txt, width=50, font=("Verdana", 18))
        hdr.pack(pady=20)

    def create_form_entry(self, label, variable, entry_type):
        # Criar uma unica entrada no formulario
        container = ttk.Frame(self.main_frame)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)
        if entry_type == "image":
            ent = ttk.Button(
                master=container, text="Procurar imagem", command=self.on_select_image
            )
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        else:
            ent = ttk.Entry(master=container, textvariable=variable)
            ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # Create a label to display the form entry
        label_entry = ttk.Label(master=container, text=variable.get())
        label_entry.pack(side=LEFT, padx=5)
        return ent

    @classmethod
    def on_select_image(cls):
        # Open a file dialog to select an image
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png")]
        )
        file_path_strip = file_path.split("/")
        cls.file_name = file_path_strip[-1]
        # Display the selected image in the GUI
        image = Image.open(file_path)
        image.save(f"{PATH}/{cls.file_name}")
        photo = ImageTk.PhotoImage(image)
        label_image = ttk.Label(master=cls.main_frame, image=photo)
        label_image.image = photo
        label_image.pack(fill=X, expand=YES)

        # Store the image path in the class variable
        cls.image_path = file_path

    def create_combobox(self, label, values_, variable):
        container = ttk.Frame(self.main_frame)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text=label, width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_combobox = ttk.Combobox(
            master=container,
            values=values_,
            textvariable=variable,
            state="readonly",
        )
        ent_combobox.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_combobox

    def textbox_description(self):
        container = ttk.Frame(self.main_frame)
        container.pack(fill=X, expand=YES, pady=5)
        lbl = ttk.Label(master=container, text="Descrição:", width=10, anchor="e")
        lbl.pack(side=LEFT, padx=5)

        ent_description = ttk.ScrolledText(master=container, wrap=WORD, height=5)
        ent_description.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent_description

    def create_buttonbox(self):
        """Caixa Botoes App"""
        container = ttk.Frame(self.main_frame)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.on_submit,
            bootstyle="SUCCESS",
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle="DANGER",
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

    @classmethod
    def on_submit(cls):
        # IMPRIME CONTEUDO E RETORNA OS VALORES
        category = cls.ctrl_category.get_by_name(cls.category.get(), cls.session)
        brand = cls.ctrl_brand.get_by_name(cls.brand.get(), cls.session)
        produto = Product()
        new_producto = produto.create(
            cls.bar_cod.get(),
            cls.name.get(),
            cls.file_name,
            cls.description.get(),
            cls.price.get(),
            brand.id,
            category.id,
        )
        cls.ctrl_product.add(new_producto, cls.session)

    # cls.category.get()

    @classmethod
    def on_cancel(cls):
        # Cancela e sai da app
        cls.quit()
