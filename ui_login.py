# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(717, 440)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(247, 247, 234);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.right_container = QFrame(self.frame)
        self.right_container.setObjectName(u"right_container")
        self.right_container.setStyleSheet(u"background-color: rgb(247, 247, 234);")
        self.right_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.right_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.right_container)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.right_container)

        self.laft_container = QFrame(self.frame)
        self.laft_container.setObjectName(u"laft_container")
        self.laft_container.setStyleSheet(u"background-color: rgb(11, 84, 48);")
        self.laft_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.laft_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.laft_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.laft_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(247, 247, 234);")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(247, 247, 234);")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.laft_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.line_user = QLineEdit(self.frame_3)
        self.line_user.setObjectName(u"line_user")
        self.line_user.setGeometry(QRect(90, 30, 181, 22))
        self.line_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.line_user.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(249, 248, 235);\n"
"color: rgb(4, 99, 51);\n"
"}\n"
"")
        self.line_pass = QLineEdit(self.frame_3)
        self.line_pass.setObjectName(u"line_pass")
        self.line_pass.setGeometry(QRect(90, 90, 181, 22))
        self.line_pass.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.line_pass.setStyleSheet(u"QLineEdit {\n"
"background-color: rgb(249, 248, 235);\n"
"color: rgb(4, 99, 51);\n"
"}\n"
"")
        self.btn_login = QPushButton(self.frame_3)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(90, 130, 181, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: rgb(88, 148, 120);\n"
"   border-radius:15px;\n"
"  color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
" \n"
"	background-color: rgb(247, 247, 234);\n"
"  border-radius:15px;\n"
"  color: rgb(11, 84, 48);\n"
"}")
        self.txt_user = QLabel(self.frame_3)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(30, 30, 49, 16))
        self.txt_user.setStyleSheet(u"color: rgb(247, 247, 234);")
        self.txt_pass = QLabel(self.frame_3)
        self.txt_pass.setObjectName(u"txt_pass")
        self.txt_pass.setGeometry(QRect(30, 90, 49, 16))
        self.txt_pass.setStyleSheet(u"color: rgb(247, 247, 234);")

        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.laft_container)


        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo_.png\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Sistema de Controle</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Login</span></p></body></html>", None))
        self.line_user.setPlaceholderText(QCoreApplication.translate("Login", u"Usu\u00e1rio", None))
        self.line_pass.setPlaceholderText(QCoreApplication.translate("Login", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.txt_user.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Usuer</span></p></body></html>", None))
        self.txt_pass.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Password</span></p></body></html>", None))
    # retranslateUi

