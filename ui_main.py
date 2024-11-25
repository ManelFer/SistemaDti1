# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(722, 413)
        Main.setStyleSheet(u"background-color: rgb(249, 248, 235);")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"  border: none;\n"
"}\n"
"\n"
"QLabel{\n"
" color:rgb(4, 99, 51);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.laft_container = QFrame(self.centralwidget)
        self.laft_container.setObjectName(u"laft_container")
        self.laft_container.setMaximumSize(QSize(200, 16777215))
        self.laft_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.laft_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.laft_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.laft_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.laft_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"\n"
"QFrame{\n"
" background-color: rgb(249, 248, 235);\n"
"}\n"
"\n"
"QToolBox{\n"
" text-align: left;\n"
" background-color: rgb(92, 148, 116);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
" border-radius: 2px;\n"
" background-color: rgb(4, 99, 51);\n"
" text-align: left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: rgb(84, 144, 124);\n"
"   border-top-left-radius:15px;\n"
"  color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"  color: rgb(4, 99, 51);\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 168, 277))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 3, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 168, 277))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.laft_container)

        self.main_conatainer = QFrame(self.centralwidget)
        self.main_conatainer.setObjectName(u"main_conatainer")
        self.main_conatainer.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_conatainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.main_conatainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_conatainer)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_conatainer)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(249, 248, 235);")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_2_cadastrar = QWidget()
        self.pg_2_cadastrar.setObjectName(u"pg_2_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_2_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_2_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
" background-color: rgb(148,148,148);\n"
" color: rgb(255,255,255);\n"
" font: 10pt\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(115, 184, 144);\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
" border-radius: 15px;\n"
" background-color: rgb(255,255,255);\n"
" font: 11pt;\n"
" color: rgb(4, 99, 51);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(115, 184, 144);\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(4, 99, 51);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(255, 85, 0);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"color: rgb(255,255,255);\n"
"background-color: rgb(218, 1, 1);\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(4, 99, 51);\n"
"backgroun-color: rgb(249, 248, 235);")

        self.verticalLayout_10.addWidget(self.label_5)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
" background-color: rgb(249, 248, 235);\n"
" color:rgb(76, 76, 76);\n"
" font: 10pt;\n"
"}\n"
"QFrame{\n"
" background-color: rgb(231,231,231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_modelo = QLineEdit(self.frame_4)
        self.txt_modelo.setObjectName(u"txt_modelo")

        self.gridLayout.addWidget(self.txt_modelo, 0, 2, 1, 1)

        self.txt_patrimonio = QLineEdit(self.frame_4)
        self.txt_patrimonio.setObjectName(u"txt_patrimonio")

        self.gridLayout.addWidget(self.txt_patrimonio, 0, 0, 1, 1)

        self.txt_marca = QLineEdit(self.frame_4)
        self.txt_marca.setObjectName(u"txt_marca")

        self.gridLayout.addWidget(self.txt_marca, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: rgb(84, 144, 124);\n"
"   border-radius:15px;\n"
"  color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"  border-radius:15px;\n"
"  color: rgb(4, 99, 51);\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_15 = QVBoxLayout(self.tab_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(4, 99, 51);\n"
"backgroun-color: rgb(249, 248, 235);")

        self.verticalLayout_15.addWidget(self.label_13)

        self.frame_7 = QFrame(self.tab_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
" background-color: rgb(249, 248, 235);\n"
" color:rgb(76, 76, 76);\n"
" font: 10pt;\n"
"}\n"
"QFrame{\n"
" background-color: rgb(231,231,231);\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_patrimonio_3_saida = QLineEdit(self.frame_7)
        self.txt_patrimonio_3_saida.setObjectName(u"txt_patrimonio_3_saida")

        self.gridLayout_2.addWidget(self.txt_patrimonio_3_saida, 0, 0, 1, 1)

        self.txt_marca_3_saida = QLineEdit(self.frame_7)
        self.txt_marca_3_saida.setObjectName(u"txt_marca_3_saida")

        self.gridLayout_2.addWidget(self.txt_marca_3_saida, 0, 1, 1, 1)

        self.txt_modelo_3_saida = QLineEdit(self.frame_7)
        self.txt_modelo_3_saida.setObjectName(u"txt_modelo_3_saida")

        self.gridLayout_2.addWidget(self.txt_modelo_3_saida, 0, 2, 1, 1)

        self.txt_n_os = QLineEdit(self.frame_7)
        self.txt_n_os.setObjectName(u"txt_n_os")

        self.gridLayout_2.addWidget(self.txt_n_os, 1, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 31))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: rgb(84, 144, 124);\n"
"   border-radius:15px;\n"
"  color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"  border-radius:15px;\n"
"  color: rgb(4, 99, 51);\n"
"}")

        self.verticalLayout_15.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_2_cadastrar)
        self.pg_4_sobre = QWidget()
        self.pg_4_sobre.setObjectName(u"pg_4_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_4_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.pg_4_sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_6 = QLabel(self.pg_4_sobre)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_11.addWidget(self.label_6)

        self.label_9 = QLabel(self.pg_4_sobre)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_4_sobre)
        self.pg_3_produtos = QWidget()
        self.pg_3_produtos.setObjectName(u"pg_3_produtos")
        self.horizontalLayout_7 = QHBoxLayout(self.pg_3_produtos)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.pg_3_produtos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.label_7 = QLabel(self.pg_3_produtos)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.Pages.addWidget(self.pg_3_produtos)
        self.pg_1_home = QWidget()
        self.pg_1_home.setObjectName(u"pg_1_home")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_1_home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.pg_1_home)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.Pages.addWidget(self.pg_1_home)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_conatainer)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_conatainer)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">DTI Controle</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("Main", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("Main", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("Main", u"Sobre", None))
        self.btn_sobre.setText(QCoreApplication.translate("Main", u"Contatos", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Main", u"Page 1", None))
        self.label_11.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Usu\u00e1rio:</span> Manoel</p><p align=\"center\"><span style=\" font-weight:700;\">Sistema:</span> Controle</p><p align=\"center\"><span style=\" font-weight:700;\">Status:</span> Ativo</p><p align=\"center\"><span style=\" font-weight:700;\">Hora:</span> hh:mm</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Main", u"Page 2", None))
        self.label.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Sistema de Controle</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Main", u"Patrimonio", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Main", u"Marca", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Main", u"Modelo", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Main", u"Quantidade", None));
        self.btn_excel.setText(QCoreApplication.translate("Main", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("Main", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("Main", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Main", u"Produtos", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Cadastrar</span></p></body></html>", None))
        self.txt_modelo.setPlaceholderText(QCoreApplication.translate("Main", u"Modelo", None))
        self.txt_patrimonio.setPlaceholderText(QCoreApplication.translate("Main", u"Patrimonio", None))
        self.txt_marca.setPlaceholderText(QCoreApplication.translate("Main", u"Marca", None))
        self.pushButton.setText(QCoreApplication.translate("Main", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Main", u"Cadastrar", None))
        self.label_13.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Sa\u00edda</span></p></body></html>", None))
        self.txt_patrimonio_3_saida.setPlaceholderText(QCoreApplication.translate("Main", u"Patrimonio", None))
        self.txt_marca_3_saida.setPlaceholderText(QCoreApplication.translate("Main", u"Marca", None))
        self.txt_modelo_3_saida.setPlaceholderText(QCoreApplication.translate("Main", u"Modelo", None))
        self.txt_n_os.setPlaceholderText(QCoreApplication.translate("Main", u"n\u00famero da Os", None))
        self.pushButton_3.setText(QCoreApplication.translate("Main", u"Retirar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Main", u"Sa\u00edda", None))
        self.label_10.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Contatos</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(79) 9 9918-9735</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">manoelferreiramatos.ti@gmail.com</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Um sistema simples usando PyQt6. Nele \u00e9 possivel fazer sistemas com o python de maneira simples e completa. Esse projeto est\u00e1 sendo usado para controle de estoque na sala de trabalho.</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Main", u"<html><head/><body><p><img src=\":/icons/icons/logo_.png\"/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo_.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"<html><head/><body><p align=\"center\">DTI Coordena\u00e7\u00e3o \u00a9 2024 Manoel Ferreira Matos.</p></body></html>", None))
    # retranslateUi

