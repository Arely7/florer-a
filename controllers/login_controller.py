from PyQt6 import QtWidgets, uic

class LoginController:
    def _init_(self, window, model):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.window.txt_username.text()
        password = self.window.txt_password.text()
        if username == "admin" and password == "123":
            self.window.login_successfull.emit()
            print("Login Correcto✔")
        else:
            QtWidgets.QMessageBox.warning(
                self.window,
                "Florería Cherry - ERROR"
                "Login Incorrecto❌"
            )
        print("Login button clicked😎😊✌👍")