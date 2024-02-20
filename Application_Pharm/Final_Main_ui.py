# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Final_Main_FFuiFF.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import Final_Main_ph_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 698)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setToolTipDuration(-1)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.Login_SignUp_Page = QWidget()
        self.Login_SignUp_Page.setObjectName(u"Login_SignUp_Page")
        self.Login_SignUp_Page.setStyleSheet(u"*{\n"
"	background-color:;\n"
"	background-image:url(:/Image_photo/Image_for_main/BGp.jpeg);\n"
"	background-size: cover;\n"
"    background-size: cover;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    height: 100vh;\n"
"    background-repeat: no-repeat;\n"
"    background-size: 100% 100%;;\n"
"\n"
"}")
        self.gridLayout = QGridLayout(self.Login_SignUp_Page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.Login_SignUp_Page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(500, 680))
        self.widget_2.setStyleSheet(u"*{\n"
"border:none;\n"
"Background-color: transparent;\n"
"Background : transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color:#ffff;\n"
"}\n"
"\n"
"#Login {\n"
"    background-color: rgba(255, 255, 255, 0.9); /* Adjust the alpha value as needed */\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"#lineEdit , #lineEdit_2 , #lineEdit_3 , #lineEdit_4 , #lineEdit_5 , #lineEdit_6 , #dateEdit , #comboBox , #lineEdit_7 , #lineEdit_8\n"
"{\n"
"   background-color :rgb(200, 200, 200); \n"
"	padding : 4px 2px;\n"
"    border-radius :5px;\n"
"\n"
"}\n"
"#pushButton , #pushButton_4 {\n"
"background-color:rgb(18, 163, 200);\n"
"    border-radius: 7px;\n"
"}\n"
"#ErrorMessage , #ErrorMessage_2 {\n"
"	color: red;\n"
"    display: inline-block;\n"
"    text-align: center;\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(490, 680))
        self.widget_3.setMaximumSize(QSize(450, 680))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Login = QWidget(self.widget_3)
        self.Login.setObjectName(u"Login")
        self.Login.setMinimumSize(QSize(420, 620))
        self.Login.setMaximumSize(QSize(420, 620))
        self.verticalLayout_4 = QVBoxLayout(self.Login)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget_2 = QStackedWidget(self.Login)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(390, 0))
        self.stackedWidget_2.setMaximumSize(QSize(420, 16777215))
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
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(215, 30))
        self.lineEdit_7.setMaximumSize(QSize(192, 27))
        font = QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)

        self.gridLayout_3.addWidget(self.lineEdit_7, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(215, 30))
        self.lineEdit_8.setMaximumSize(QSize(150, 27))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.lineEdit_8, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.LoginPage)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(124, 150))
        self.widget_4.setMaximumSize(QSize(225, 16777215))
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 50, 66, 65))
        self.label_9.setMinimumSize(QSize(64, 64))
        self.label_9.setMaximumSize(QSize(66, 66))
        self.label_9.setPixmap(QPixmap(u":/Icon_custom/Image_for_main/icon_custom/login.png"))
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 130, 91, 31))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_10.setFont(font1)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(35, 170, 171, 20))
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.widget_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.LoginPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(209, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(103, 131, 170, 25))
        self.pushButton_3.setMinimumSize(QSize(170, 25))
        self.pushButton_3.setMaximumSize(QSize(160, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setUnderline(True)
        self.pushButton_3.setFont(font2)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(117, 70, 140, 30))
        self.pushButton_4.setMinimumSize(QSize(140, 30))
        self.pushButton_4.setMaximumSize(QSize(140, 28))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton_4.setFont(font3)
        self.ErrorMessage_2 = QLabel(self.frame_3)
        self.ErrorMessage_2.setObjectName(u"ErrorMessage_2")
        self.ErrorMessage_2.setGeometry(QRect(50, 0, 271, 20))
        self.ErrorMessage_2.setWordWrap(True)

        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.LoginPage)
        self.RegisterPage = QWidget()
        self.RegisterPage.setObjectName(u"RegisterPage")
        self.widget_5 = QWidget(self.RegisterPage)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(100, 11, 201, 131))
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 0, 61, 61))
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/Icon_custom/Image_for_main/icon_custom/add-friend50px.png"))
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 91, 31))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 107, 171, 20))
        self.label_3.setFont(font)
        self.frame = QFrame(self.RegisterPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 150, 391, 351))
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
        self.lineEdit.setGeometry(QRect(9, 17, 170, 27))
        self.lineEdit.setMinimumSize(QSize(170, 27))
        self.lineEdit.setMaximumSize(QSize(130, 27))
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(210, 17, 170, 27))
        self.lineEdit_4.setMinimumSize(QSize(170, 27))
        self.lineEdit_4.setMaximumSize(QSize(130, 27))
        self.lineEdit_4.setFont(font)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 229, 201, 16))
        self.label_4.setFont(font)
        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(248, 222, 121, 26))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 270, 195, 16))
        self.label_5.setFont(font)
        self.radioButton_Dr = QRadioButton(self.frame)
        self.radioButton_Dr.setObjectName(u"radioButton_Dr")
        self.radioButton_Dr.setGeometry(QRect(20, 292, 82, 17))
        self.radioButton_pharm = QRadioButton(self.frame)
        self.radioButton_pharm.setObjectName(u"radioButton_pharm")
        self.radioButton_pharm.setGeometry(QRect(110, 292, 82, 17))
        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(240, 290, 121, 21))
        font4 = QFont()
        font4.setPointSize(8)
        self.comboBox.setFont(font4)
        self.pushButton = QPushButton(self.RegisterPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 523, 125, 28))
        self.pushButton.setMinimumSize(QSize(125, 28))
        self.pushButton.setMaximumSize(QSize(125, 28))
        self.pushButton.setFont(font3)
        self.pushButton_2 = QPushButton(self.RegisterPage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 566, 160, 25))
        self.pushButton_2.setMinimumSize(QSize(160, 25))
        self.pushButton_2.setMaximumSize(QSize(160, 25))
        self.pushButton_2.setFont(font2)
        self.ErrorMessage = QLabel(self.RegisterPage)
        self.ErrorMessage.setObjectName(u"ErrorMessage")
        self.ErrorMessage.setGeometry(QRect(60, 490, 271, 20))
        self.ErrorMessage.setWordWrap(True)
        self.stackedWidget_2.addWidget(self.RegisterPage)

        self.verticalLayout_4.addWidget(self.stackedWidget_2, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.Login)


        self.verticalLayout_5.addWidget(self.widget_3, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.Login_SignUp_Page)
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.Main_page.setStyleSheet(u"#frame_4 \n"
"{\n"
"background-color : rgb(255, 255, 255) ;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.Main_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.Main_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.frame_4)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(101, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_13 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.leftMenuSubContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame_6)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(19, 0))
        self.menuBtn.setMaximumSize(QSize(101, 16777215))
        icon = QIcon()
        icon.addFile(u":/Icon_web/Image_for_main/icons_from_Web/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_13.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.leftMenuSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_7)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(19, 0))
        self.homeBtn.setMaximumSize(QSize(101, 16777215))
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"background-color: rgb(18, 163, 176) ;")
        icon1 = QIcon()
        icon1.addFile(u":/Icon_web/Image_for_main/icons_from_Web/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.homeBtn)

        self.orderBtn = QPushButton(self.frame_7)
        self.orderBtn.setObjectName(u"orderBtn")
        self.orderBtn.setMinimumSize(QSize(19, 0))
        self.orderBtn.setMaximumSize(QSize(101, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/Icon_web/Image_for_main/icons_from_Web/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderBtn.setIcon(icon2)
        self.orderBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.orderBtn)

        self.reportsBtn = QPushButton(self.frame_7)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setMinimumSize(QSize(19, 0))
        self.reportsBtn.setMaximumSize(QSize(101, 16777215))
        icon3 = QIcon()
        icon3.addFile(u":/Icon_web/Image_for_main/icons_from_Web/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon3)
        self.reportsBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.reportsBtn)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.frame_8 = QFrame(self.leftMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_8)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_8)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(19, 0))
        self.settingsBtn.setMaximumSize(QSize(101, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/Icon_web/Image_for_main/icons_from_Web/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_8)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(19, 0))
        self.infoBtn.setMaximumSize(QSize(101, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/Icon_web/Image_for_main/icons_from_Web/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_8)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(19, 0))
        self.helpBtn.setMaximumSize(QSize(101, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/Icon_web/Image_for_main/icons_from_Web/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.helpBtn)


        self.verticalLayout_13.addWidget(self.frame_8, 0, Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.leftMenuSubContainer)


        self.gridLayout_5.addWidget(self.leftMenuContainer, 0, 0, 1, 1)

        self.centerMenuContatiner = QWidget(self.frame_4)
        self.centerMenuContatiner.setObjectName(u"centerMenuContatiner")
        self.centerMenuContatiner.setMinimumSize(QSize(100, 0))
        self.centerMenuContatiner.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuContatiner)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContatiner)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuSubContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.frame_5 = QFrame(self.centerMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 1)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.closeCenterMenuBtn = QPushButton(self.frame_5)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon7 = QIcon()
        icon7.addFile(u":/Icon_web/Image_for_main/icons_from_Web/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon7)
        self.closeCenterMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.centerMenuPages = QStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.centerMenuPages.setMinimumSize(QSize(0, 0))
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_9 = QVBoxLayout(self.settingPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.settingPage)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setPointSize(13)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.centerMenuPages.addWidget(self.settingPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.helpPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)

        self.centerMenuPages.addWidget(self.helpPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_11 = QVBoxLayout(self.infoPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.infoPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.centerMenuPages.addWidget(self.infoPage)

        self.verticalLayout_8.addWidget(self.centerMenuPages)


        self.verticalLayout_7.addWidget(self.centerMenuSubContainer)


        self.gridLayout_5.addWidget(self.centerMenuContatiner, 0, 1, 1, 1)

        self.mainbodyContainer = QWidget(self.frame_4)
        self.mainbodyContainer.setObjectName(u"mainbodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbodyContainer.sizePolicy().hasHeightForWidth())
        self.mainbodyContainer.setSizePolicy(sizePolicy1)
        self.mainbodyContainer.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.mainbodyContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainbodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.gridLayout_6 = QGridLayout(self.headerContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_9 = QFrame(self.headerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(40, 40))
        self.label_13.setPixmap(QPixmap(u":/icon/Image/icons/pharmacy.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        self.label_14.setFont(font6)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)

        self.frame_10 = QFrame(self.headerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_10)
        self.notificationBtn.setObjectName(u"notificationBtn")
        icon8 = QIcon()
        icon8.addFile(u":/Icon_web/Image_for_main/icons_from_Web/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_10)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/Icon_web/Image_for_main/icons_from_Web/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon9)
        self.moreMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn, 0, Qt.AlignRight)

        self.profileMenuBtn = QPushButton(self.frame_10)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/Icon_web/Image_for_main/icons_from_Web/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon10)
        self.profileMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn, 0, Qt.AlignRight)


        self.gridLayout_6.addWidget(self.frame_10, 0, 1, 1, 1)

        self.frame_11 = QFrame(self.headerContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.frame_11, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainbodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(574, 321))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContatiner = QWidget(self.mainBodyContent)
        self.mainContentsContatiner.setObjectName(u"mainContentsContatiner")
        self.verticalLayout_17 = QVBoxLayout(self.mainContentsContatiner)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.mainPages = QStackedWidget(self.mainContentsContatiner)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.gridLayout_4 = QGridLayout(self.homePage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Home_Frame = QFrame(self.homePage)
        self.Home_Frame.setObjectName(u"Home_Frame")
        self.Home_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Home_Frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(15)
        self.Cared_2 = QFrame(self.Home_Frame)
        self.Cared_2.setObjectName(u"Cared_2")
        self.Cared_2.setMinimumSize(QSize(50, 90))
        self.Cared_2.setAutoFillBackground(True)
        self.Cared_2.setFrameShape(QFrame.StyledPanel)
        self.Cared_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Cared_2, 0, 1, 1, 1)

        self.Cared_5 = QFrame(self.Home_Frame)
        self.Cared_5.setObjectName(u"Cared_5")
        self.Cared_5.setMinimumSize(QSize(50, 80))
        self.Cared_5.setAutoFillBackground(True)
        self.Cared_5.setFrameShape(QFrame.StyledPanel)
        self.Cared_5.setFrameShadow(QFrame.Raised)
        self.Cared_7 = QFrame(self.Cared_5)
        self.Cared_7.setObjectName(u"Cared_7")
        self.Cared_7.setGeometry(QRect(10, 0, 102, 90))
        self.Cared_7.setMinimumSize(QSize(50, 90))
        self.Cared_7.setAutoFillBackground(True)
        self.Cared_7.setFrameShape(QFrame.StyledPanel)
        self.Cared_7.setFrameShadow(QFrame.Raised)
        self.Card_2 = QFrame(self.Cared_5)
        self.Card_2.setObjectName(u"Card_2")
        self.Card_2.setGeometry(QRect(-98, -95, 102, 80))
        self.Card_2.setMinimumSize(QSize(50, 80))
        self.Card_2.setAutoFillBackground(True)
        self.Card_2.setFrameShape(QFrame.StyledPanel)
        self.Card_2.setFrameShadow(QFrame.Raised)
        self.Cared_8 = QFrame(self.Cared_5)
        self.Cared_8.setObjectName(u"Cared_8")
        self.Cared_8.setGeometry(QRect(-98, 0, 102, 80))
        self.Cared_8.setMinimumSize(QSize(50, 80))
        self.Cared_8.setAutoFillBackground(True)
        self.Cared_8.setFrameShape(QFrame.StyledPanel)
        self.Cared_8.setFrameShadow(QFrame.Raised)
        self.Cared_9 = QFrame(self.Cared_5)
        self.Cared_9.setObjectName(u"Cared_9")
        self.Cared_9.setGeometry(QRect(118, -95, 102, 80))
        self.Cared_9.setMinimumSize(QSize(50, 80))
        self.Cared_9.setAutoFillBackground(True)
        self.Cared_9.setFrameShape(QFrame.StyledPanel)
        self.Cared_9.setFrameShadow(QFrame.Raised)
        self.Cared_10 = QFrame(self.Cared_5)
        self.Cared_10.setObjectName(u"Cared_10")
        self.Cared_10.setGeometry(QRect(10, -95, 102, 80))
        self.Cared_10.setMinimumSize(QSize(50, 80))
        self.Cared_10.setAutoFillBackground(True)
        self.Cared_10.setFrameShape(QFrame.StyledPanel)
        self.Cared_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Cared_5, 1, 1, 1, 1)

        self.Card_1 = QFrame(self.Home_Frame)
        self.Card_1.setObjectName(u"Card_1")
        self.Card_1.setMinimumSize(QSize(50, 90))
        self.Card_1.setAutoFillBackground(True)
        self.Card_1.setFrameShape(QFrame.StyledPanel)
        self.Card_1.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Card_1, 0, 0, 1, 1)

        self.Cared_4 = QFrame(self.Home_Frame)
        self.Cared_4.setObjectName(u"Cared_4")
        self.Cared_4.setMinimumSize(QSize(50, 90))
        self.Cared_4.setAutoFillBackground(True)
        self.Cared_4.setFrameShape(QFrame.StyledPanel)
        self.Cared_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Cared_4, 1, 0, 1, 1)

        self.Cared_6 = QFrame(self.Home_Frame)
        self.Cared_6.setObjectName(u"Cared_6")
        self.Cared_6.setMinimumSize(QSize(50, 90))
        self.Cared_6.setAutoFillBackground(True)
        self.Cared_6.setFrameShape(QFrame.StyledPanel)
        self.Cared_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Cared_6, 1, 2, 1, 1)

        self.Cared_3 = QFrame(self.Home_Frame)
        self.Cared_3.setObjectName(u"Cared_3")
        self.Cared_3.setMinimumSize(QSize(50, 90))
        self.Cared_3.setAutoFillBackground(True)
        self.Cared_3.setFrameShape(QFrame.StyledPanel)
        self.Cared_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.Cared_3, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Home_Frame, 0, 0, 1, 1)

        self.mainPages.addWidget(self.homePage)
        self.orderPage = QWidget()
        self.orderPage.setObjectName(u"orderPage")
        self.verticalLayout_18 = QVBoxLayout(self.orderPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_16 = QLabel(self.orderPage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_16)

        self.mainPages.addWidget(self.orderPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_19 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_17 = QLabel(self.reportsPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_17)

        self.mainPages.addWidget(self.reportsPage)

        self.verticalLayout_17.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContatiner)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(200, 321))
        self.verticalLayout_20 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuSubContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.frame_13 = QFrame(self.rightMenuSubContainer)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.closeRightMenuBtn = QPushButton(self.frame_13)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon7)
        self.closeRightMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.rightMenuPages = QStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_22 = QVBoxLayout(self.profilePage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_19 = QLabel(self.profilePage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_19)

        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_23 = QVBoxLayout(self.morePage)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_20 = QLabel(self.morePage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_20)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_21.addWidget(self.rightMenuPages)


        self.verticalLayout_20.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QWidget(self.mainbodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.popupNotificationContainer.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_24 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_24.setSpacing(9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_25 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_21 = QLabel(self.popupNotificationSubContainer)
        self.label_21.setObjectName(u"label_21")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.label_21.setFont(font7)

        self.verticalLayout_25.addWidget(self.label_21)

        self.frame_14 = QFrame(self.popupNotificationSubContainer)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        font8 = QFont()
        font8.setBold(False)
        self.label_22.setFont(font8)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)

        self.closeNotificationBtn = QPushButton(self.frame_14)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon11 = QIcon()
        icon11.addFile(u":/Icon_web/Image_for_main/icons_from_Web/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon11)
        self.closeNotificationBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn)


        self.verticalLayout_25.addWidget(self.frame_14)


        self.verticalLayout_24.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_16.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainbodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_12 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_16.addWidget(self.footerContainer)


        self.gridLayout_5.addWidget(self.mainbodyContainer, 0, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.Main_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


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
        self.ErrorMessage_2.setText("")
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
        self.radioButton_Dr.setText(QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.radioButton_pharm.setText(QCoreApplication.translate("MainWindow", u"Pharmacist", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Hepatology\n"
"", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Neurology\n"
"", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Obstetrics and Gynecology", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Internal Medicine\n"
"", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Orthopedics\n"
"", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Pediatrics\n"
"", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Urology", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gastroenterology\n"
"", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Ophthalmology", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"ENT (Ear, Nose, and Throat)", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Already Registarard ? Login", None))
        self.ErrorMessage.setText("")
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
#if QT_CONFIG(tooltip)
        self.orderBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Order", None))
#endif // QT_CONFIG(tooltip)
        self.orderBtn.setText(QCoreApplication.translate("MainWindow", u" Order", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u" Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Informations", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u" Help", None))
#if QT_CONFIG(statustip)
        self.centerMenuContatiner.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Smart Pharmacy", None))
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Notifications Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
    # retranslateUi

