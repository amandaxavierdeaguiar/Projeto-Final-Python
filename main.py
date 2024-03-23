from controllers.UserController import UserController
from models.Enums.TypeAccess import TypeAccess
from models.User import User
from views.BaseWindow import BaseWindow
from views.LoginView import LoginView


def main():
    app = BaseWindow(
        "Login",
        "cosmo",
        background="#EBEBEB",
        resizable=(True, True),
        size=[856, 645],
        minsize=[600, 400],
    )
    LoginView(app)
    app.mainloop()


if __name__ == "__main__":
    main()
