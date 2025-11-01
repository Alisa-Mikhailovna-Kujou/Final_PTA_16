from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import os

class Login(QMainWindow):
    def  __init__(self):
        super().__init__()
        uic.loadUI("Login.ui", self)
        self.Create_acc.clicked.connect(self.show_register)
        self.Login_button.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def check_login(self):
        email = self.Enter_email_login.text()
        password = self.Enter_password_login.text()
        if email == "admin" and password == "admin":
            main.show()
            self.close()
    def show_register(self):
        register.show()
        self.close()

class Registe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Register.ui", self)
        self.Register_button.clicked.connect(self.register_user)
        self.Back_to_login.clicked.connect(self.back_to_login)
        self.msg_box = QMessageBox()

    def back_to_login(self):
        login.show()
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Main.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    register = Registe()
    main = Main()
    login.show()
    app.exec()