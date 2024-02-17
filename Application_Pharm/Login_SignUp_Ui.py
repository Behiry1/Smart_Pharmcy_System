# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_SignUp.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resFile_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(885, 741)
        MainWindow.setMinimumSize(QSize(720, 500))
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"Background-color: transparent;\n"
"Background : transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color:#ffff;\n"
"}\n"
"#centralwidget{\n"
"	background-color:;\n"
"	background-image:url(:/Image/BGp.jpeg);\n"
"	background-size: cover;\n"
"    background-size: cover;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    height: 100vh;\n"
"    background-repeat: no-repeat;\n"
"    background-size: 100% 100%;;\n"
"\n"
"}\n"
"#Login {\n"
"    background-color: rgba(255, 255, 255, 0.9); /* Adjust the alpha value as needed */\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#lineEdit , #lineEdit_2 , #lineEdit_3 , #lineEdit_4 , #lineEdit_5 , #lineEdit_6 , #dateEdit , #comboBox , #lineEdit_7 , #lineEdit_8\n"
"{\n"
"   background-color :rgb(200, 200, 200); \n"
"	padding : 5px 3px;\n"
"    border-radius :5px;\n"
"\n"
"}\n"
"#pushButton , #pushButton_4 {\n"
"background-color : rgb(20, 180, 196);\n"
"    border-radius: 7px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(490, 680))
        self.widget_2.setMaximumSize(QSize(450, 680))
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Login = QWidget(self.widget_2)
        self.Login.setObjectName(u"Login")
        self.Login.setMinimumSize(QSize(400, 580))
        self.Login.setMaximumSize(QSize(400, 580))
        self.verticalLayout_4 = QVBoxLayout(self.Login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.Login)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(390, 0))
        self.stackedWidget.setMaximumSize(QSize(400, 16777215))
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.gridLayout_2 = QGridLayout(self.LoginPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.LoginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 135))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(190, 30))
        self.lineEdit_7.setMaximumSize(QSize(150, 27))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(190, 30))
        self.lineEdit_8.setMaximumSize(QSize(150, 27))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_8, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.widget_3 = QWidget(self.LoginPage)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(124, 150))
        self.widget_3.setMaximumSize(QSize(225, 16777215))
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 10, 61, 61))
        self.label_9.setMinimumSize(QSize(50, 50))
        self.label_9.setMaximumSize(QSize(64, 64))
        self.label_9.setPixmap(QPixmap(u":/icon/Image/icons/add-friend50px.png"))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(65, 80, 91, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_10.setFont(font1)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 120, 171, 20))
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.LoginPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(209, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(19, 109, 170, 25))
        self.pushButton_3.setMinimumSize(QSize(170, 25))
        self.pushButton_3.setMaximumSize(QSize(160, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(True)
        self.pushButton_3.setFont(font2)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 40, 125, 28))
        self.pushButton_4.setMinimumSize(QSize(125, 28))
        self.pushButton_4.setMaximumSize(QSize(125, 28))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_4.setFont(font3)

        self.gridLayout_2.addWidget(self.frame_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.LoginPage)
        self.RegisterPage = QWidget()
        self.RegisterPage.setObjectName(u"RegisterPage")
        self.widget = QWidget(self.RegisterPage)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 11, 201, 131))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 61, 61))
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/icon/Image/icons/add-friend50px.png"))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 91, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 107, 171, 20))
        self.label_3.setFont(font)
        self.frame = QFrame(self.RegisterPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 160, 371, 311))
        self.frame.setStyleSheet(u"*{\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(9, 140, 170, 27))
        self.lineEdit_2.setMinimumSize(QSize(170, 27))
        self.lineEdit_2.setMaximumSize(QSize(150, 27))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(9, 181, 170, 27))
        self.lineEdit_3.setMinimumSize(QSize(170, 27))
        self.lineEdit_3.setMaximumSize(QSize(170, 27))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(9, 58, 170, 27))
        self.lineEdit_5.setMinimumSize(QSize(170, 27))
        self.lineEdit_5.setMaximumSize(QSize(150, 27))
        self.lineEdit_5.setFont(font)
        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(9, 99, 170, 27))
        self.lineEdit_6.setMinimumSize(QSize(170, 27))
        self.lineEdit_6.setMaximumSize(QSize(150, 27))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setEchoMode(QLineEdit.Normal)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(9, 17, 130, 27))
        self.lineEdit.setMinimumSize(QSize(130, 27))
        self.lineEdit.setMaximumSize(QSize(130, 27))
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(210, 17, 130, 27))
        self.lineEdit_4.setMinimumSize(QSize(130, 27))
        self.lineEdit_4.setMaximumSize(QSize(130, 27))
        self.lineEdit_4.setFont(font)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 229, 201, 16))
        self.label_4.setFont(font)
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(228, 222, 121, 26))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 272, 195, 16))
        self.label_5.setFont(font)
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(227, 270, 121, 26))
        self.pushButton = QPushButton(self.RegisterPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 476, 125, 28))
        self.pushButton.setMinimumSize(QSize(125, 28))
        self.pushButton.setMaximumSize(QSize(125, 28))
        self.pushButton.setFont(font3)
        self.pushButton_2 = QPushButton(self.RegisterPage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 520, 160, 25))
        self.pushButton_2.setMinimumSize(QSize(160, 25))
        self.pushButton_2.setMaximumSize(QSize(160, 25))
        self.pushButton_2.setFont(font2)
        self.stackedWidget.addWidget(self.RegisterPage)

        self.verticalLayout_4.addWidget(self.stackedWidget, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.Login)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 885, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email@exampl.com", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Enter you Informatoin below", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Not Registarard ? Register ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter you Informatoin below", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email@exampl.com", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Firstname", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date of birth : mm/dd/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Are you a doctor or a pharmacist?", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pharmacist", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Already Registarard ? Login", None))
    # retranslateUi

