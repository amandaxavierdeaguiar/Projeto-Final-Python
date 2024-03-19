from controllers.ProductController import ProductController
from controllers.StockController import StockController
from models.db.db_conection import get_session
from sqlmodel import Session
from customtkinter import *
from CTkTable import CTkTable


class StockView:
    ctrl_stock: StockController = StockController()
    ctrl_product: ProductController = ProductController()
    session: Session = get_session()

    def __init__(self):
        super().__init__()

    @classmethod
    def give_frame(cls, app_: CTk) -> CTkFrame:
        frame = CTkFrame(app_, fg_color="#fff", width=680, height=650, corner_radius=0)
        frame.pack_propagate(False)
        frame.pack(side="left")

        title_frame = CTkFrame(master=frame, fg_color="transparent")
        title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        # =========== TITULO STOCK ===========
        CTkLabel(
            master=title_frame, text="Stock", font=("Verdana", 30), text_color="#045A87"
        ).pack(anchor="nw", side="left")

        # Add novos produtos
        CTkButton(
            master=title_frame,
            text="+ Novos Produtos",
            font=("Verdana", 15),
            text_color="#fff",
            fg_color="#008DD2",
            hover_color="#045A87",
            cursor="hand2",
        ).pack(anchor="ne", side="right")

        # Botão Pesquisar produto
        search_container = CTkFrame(master=frame, height=50, fg_color="#A9DCF6")
        search_container.pack(fill="x", pady=(45, 0), padx=27)

        # Botao pesquisa de produto
        CTkEntry(
            master=search_container,
            width=305,
            placeholder_text="Pesquise o produto",
            border_color="#008DD2",
            border_width=2,
        ).pack(side="left", padx=(13, 0), pady=15)

        # Pesquisar por data
        cls.box_date = CTkComboBox(
            master=search_container,
            width=125,
            values=["Date", "Data Recentes", "Data antigas"],
            button_color="#008DD2",  # Botao Ordem Data
            border_color="#008DD2",
            border_width=2,
            button_hover_color="#045A87",  # Botao data  hover
            dropdown_hover_color="#045A87",  # Dentro
            dropdown_fg_color="#008DD2",
            dropdown_text_color="#fff",
        ).pack(side="left", padx=(13, 0), pady=15)

        cls.box_status = CTkComboBox(
            master=search_container,
            width=125,
            values=["Pesquisar:", "Nome", "ID", "Descrição", "Fornecedor"],
            button_color="#008DD2",
            border_color="#008DD2",
            border_width=2,
            button_hover_color="#045A87",
            dropdown_hover_color="#045A87",
            dropdown_fg_color="#008DD2",
            dropdown_text_color="#fff",
        ).pack(side="left", padx=(13, 0), pady=15)

        # PRODUTOS(IMPORTAR DA DATABASE) E DAR MERGE
        table_data = cls.ctrl_stock.get_all(cls.session)
        table_data2 = cls.ctrl_product.get_all_join(cls.session)
        x, result, r_temp = 0, [], []
        while x < len(table_data):
            r_temp = [x for x in table_data2[x]]
            r_temp.append(table_data[x][1])
            result.append(r_temp)
            x += 1
        header = ["Bar Code", "Product Name", "Brand", "Category", "Price", "Quantity"]
        result.insert(0, header)

        # Definições Tabela
        table_frame = CTkScrollableFrame(master=frame, fg_color="transparent")
        table_frame.pack(expand=True, fill="both", padx=27, pady=21)
        table = CTkTable(
            master=table_frame,
            values=result,
            colors=["#E6E6E6", "#EEEEEE"],
            header_color="#008DD2",
            hover_color="#B4B4B4",
        )
        table.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        table.pack(expand=True)

        return frame
