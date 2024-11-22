from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox)
from PySide6.QtGui import QIcon
from ui_login import Ui_Login
from ui_main import Ui_Main
import sys

class Login(QMainWindow, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DTI - Sistema de controle")
        appIcon = QIcon(u"src_img/icons/")
        self.setWindowIcon(appIcon)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()