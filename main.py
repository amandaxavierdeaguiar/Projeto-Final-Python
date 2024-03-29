import hashlib
from pathlib import Path
from views.Base.BaseWindow import BaseWindow
from views.MainView import MainView

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
    MainView(app)
    app.mainloop()


def hash_password(pwd):
    """Hash a password using SHA-256 algorithm"""
    pwd_bytes = pwd.encode("utf-8")
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd


if __name__ == "__main__":
    main()
