from typing import Any

from controllers.ProductController import ProductController
from controllers.StockController import StockController
from models.Enums.TypeSearch import TypeSearch
from models.UserAuthentication import UserAuthentication
from models.db.db_conection import get_session
from sqlmodel import Session
from customtkinter import *
from CTkTable import CTkTable


class StockView:
    table_data = None
    frame: CTkFrame
    ctrl_stock: StockController = StockController()
    ctrl_product: ProductController = ProductController()
    choice_search: CTkComboBox
    box_search: CTkEntry
    header_table: CTkTable
    table: CTkTable
    table_frame: CTkScrollableFrame
    session: Session = get_session()
    user: UserAuthentication

    def __init__(self, app_, user_: UserAuthentication):
        self.user = user_
        super().__init__()
        self.create_frame(app_, self.user)

    @classmethod
    def create_frame(cls, app_, user_: UserAuthentication):
        cls.frame = CTkFrame(
            app_, fg_color="#fff", width=680, height=650, corner_radius=0
        )
        cls.frame.pack_propagate(False)
        cls.frame.pack(side="left")

        title_frame = CTkFrame(master=cls.frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        # =========== TITULO STOCK ===========
        CTkLabel(
            master=title_frame, text="Stock", font=("Verdana", 30), text_color="#045A87"
        ).pack(anchor="nw", side="left")

        # Add novos produtos
        if "Create" in user_.permissions["Stock"]:
            CTkButton(
                master=title_frame,
                text="+ Novos Produtos",
                font=("Verdana", 15),
                text_color="#fff",
                fg_color="#008DD2",
                hover_color="#045A87",
                cursor="hand2",
            ).pack(anchor="ne", side="right")
        else:
            CTkButton(
                master=title_frame,
                text="+ Novos Produtos",
                font=("Verdana", 15),
                text_color="#fff",
                fg_color="#008DD2",
                hover_color="#045A87",
                cursor="hand2",
                state="disabled",
            ).pack(anchor="ne", side="right")

        search_container = CTkFrame(master=cls.frame, height=50, fg_color="#A9DCF6")
        search_container.pack(fill="x", pady=(45, 0), padx=27)

        cls.box_search = CTkEntry(
            master=search_container,
            width=305,
            placeholder_text="Pesquise o produto",
            border_color="#008DD2",
            border_width=2,
        )
        cls.box_search.pack(side="left", padx=(13, 0), pady=15)

        cls.choice_search = CTkComboBox(
            master=search_container,
            width=125,
            values=["Pesquisar:", "Nome", "Bar Code", "Categoria", "Marca"],
            button_color="#008DD2",
            border_color="#008DD2",
            border_width=2,
            button_hover_color="#045A87",
            dropdown_hover_color="#045A87",
            dropdown_fg_color="#008DD2",
            dropdown_text_color="#fff",
        )
        cls.choice_search.pack(side="left", padx=(13, 0), pady=15)

        CTkButton(
            master=search_container,
            text="Pesquisar",
            font=("Verdana", 15),
            text_color="#fff",
            fg_color="#008DD2",
            hover_color="#045A87",
            cursor="hand2",
            state="normal",
            command=cls.call_search,
        ).pack(side="left", padx=(13, 0), pady=15)

    @classmethod
    def call_search(cls):
        cls.table_frame.destroy()
        cls.table.destroy()
        cls.get_frame()

    @classmethod
    def get_frame(cls) -> CTkFrame:
        # PRODUTOS(IMPORTAR DA DATABASE) E DAR MERGE
        cls.table_data = cls.ctrl_stock.get_all(cls.session)
        header = ["Bar Code", "Product Name", "Brand", "Category", "Price", "Quantity"]
        cls.table_data.insert(0, header)
        # Definições Tabela
        cls.table_frame = CTkScrollableFrame(master=cls.frame, fg_color="transparent")
        cls.table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        cls.table = CTkTable(
            master=cls.table_frame,
            values=header,
            colors=["#E6E6E6", "#EEEEEE"],
            header_color="#008DD2",
            hover_color="#B4B4B4",
        )
        cls.table.edit_row(0, text_color="#fff", hover_color="#045A87")
        cls.table = CTkTable(
            master=cls.table_frame,
            values=cls.table_data,
            colors=["#E6E6E6", "#EEEEEE"],
            header_color="#008DD2",
            hover_color="#B4B4B4",
        )

        cls.table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        cls.table.pack(expand=True)
        return cls.frame
