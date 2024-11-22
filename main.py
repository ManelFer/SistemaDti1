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

    def open_system(self):
        if self.line_pass.text() == '123':
            self.w = Ui_Main()
            self.w.show()
            self.close()
        else:
            print('Senha inválida')

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DTI - Sistema de controle")

        #****************PAGINAS DO SISTEMA****************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_1_home))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()