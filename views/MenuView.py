import customtkinter
from PIL import Image
import os
from customtkinter import *


class MenuView:
    app: CTk = CTk()
    menu_frame: CTkFrame
    btn_login: CTkButton
    logo_img: CTkImage
    logo_img_path: Image
    menu_logo: CTkLabel
    error_txt: str = ""

    def __init__(self):
        super().__init__()

    @classmethod
    def create_button(cls, frame_, img_, text_, command_) -> CTkButton:
        path_img = Image.open(f"{img_}")
        btn_img = CTkImage(dark_image=path_img, light_image=path_img)
        btn_temp = CTkButton(
            master=frame_,
            image=btn_img,
            text=f"{text_}",
            fg_color="transparent",
            font=("Verdana", 14),
            hover_color="#045A87",
            anchor="w",
            command=command_,
            state="disabled",
        )
        btn_temp.pack(anchor="center", ipady=5, pady=(60, 0))
        return btn_temp

    @classmethod
    def sidebar(cls, app_):
        # Criando Frame do Menu
        cls.menu_frame = CTkFrame(
            master=app_, fg_color="#008DD2", width=176, height=650, corner_radius=0
        )
        cls.menu_frame.pack_propagate(False)
        cls.menu_frame.pack(fill="y", anchor="w", side="left")

        # logo do menu
        cls.logo_img_path = Image.open("view/assets/logo-stock-b.png")
        cls.logo_img = CTkImage(
            dark_image=cls.logo_img_path,
            light_image=cls.logo_img_path,
            size=(77.68, 85.42),
        )

        # Colocando e Posicionando a Logo
        cls.menu_logo = CTkLabel(master=cls.menu_frame, image=cls.logo_img)
        cls.menu_logo.pack(pady=(48, 0), anchor="center")
        return cls.menu_frame


if __name__ == "__main__":
    MenuView()
