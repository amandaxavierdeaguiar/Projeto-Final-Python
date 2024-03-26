from pathlib import Path

from views.Base.BaseWindow import BaseWindow
from views.Login.LoginView import LoginView

PATH = Path(__file__).parent / "views/assets"


def main():
    app = BaseWindow(
        title="Stock Management",
        themename="cosmo",
        iconphoto=f"{PATH}/icons/logo-stock.png",
        background="#EBEBEB",
        resizable=(True, True),
        size=[856, 645],
        minsize=[600, 400],
    )
    LoginView(app)
    app.mainloop()


if __name__ == "__main__":
    main()
