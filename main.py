from PyQt6 import QtWidgets, uic
import sys
from login_controller import LoginController
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPalette

class Login(QtWidgets.QMainWindow):
    login_successfull = pyqtSignal()

    def _init_(self):
        super()._init_()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self,self)
        self.apply_theme

    def apply_theme(self):
        is_dark = self.palette().color(QPalette.ColorRole.Window).lightness() <128
        print(f"drak: {is_dark}")
        
class Sell(QtWidgets.QMainWindow):
    def _init_(self):
        super()._init_()
        uic.loadUi("./views/main.ui", self)

class AppManager:
    def _init_(self):
        self.login_window=Login()
        self.sell_window= Sell()
        self.login_window.login_successfull.connect(self.show_main_window)
        self.login_window.show()
    
    def show_main_window(self):
        self.sell_window.show()
        self.login_window.close()

app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())