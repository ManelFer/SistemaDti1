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
        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):
        if self.line_pass.text() == '123':
            self.main_window = Main()
            self.main_window.show()
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
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_2_cadastrar))
        self.btn_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_3_produtos)) # tem um error nessa parte, os nomes estão trocados com o sobre e não é produtos é sobre
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_4_sobre))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()