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
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import Final_Main_ph_rc
import Final_Main_ph_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 698)
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
        self.label_11.setGeometry(QRect(15, 170, 201, 20))
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
        self.Main_page.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"padding: 0;\n"
"margin: 0;\n"
"color: #fff;\n"
"}\n"
"#centralwidget {\n"
"background-color: #064666;\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color: #064666;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align: left;\n"
"padding : 5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"background-color: #064666;\n"
"}\n"
"#popupNotificationSubContainer {\n"
"background-color: #064666;\n"
"border-radius:10px ;\n"
"}\n"
"#headerContainer,#footerContainer{\n"
"background-color: #064666;\n"
"}\n"
"\n"
"#frame_4 , #frame_8 {\n"
"background-color: #ffff;\n"
"border-radius:10px ;\n"
"}\n"
"\n"
"#leftMenuContainer {\n"
"padding-top: 20px;\n"
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
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mainbodyContainer = QWidget(self.frame_4)
        self.mainbodyContainer.setObjectName(u"mainbodyContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainbodyContainer.sizePolicy().hasHeightForWidth())
        self.mainbodyContainer.setSizePolicy(sizePolicy)
        self.mainbodyContainer.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.mainbodyContainer)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainbodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"/* Styling for QPushButton */\n"
"QPushButton {\n"
"    background-color:transparent; /* Default background color */\n"
"    color: black; /* Text color */\n"
" 	border: 1px solid transparent ;\n"
"    padding: 1px 2px; /* Padding */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Styling for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 163, 176); /* Background color on hover */\n"
"\n"
"}\n"
"\n"
"/* Styling for QFrame (the container) */\n"
"QFrame {\n"
"    background-color: transparent; /* Transparent background */\n"
"     /* No border */\n"
"	padding : 2px;\n"
"}\n"
"*{\n"
"background-color : #02202f;\n"
"}")
        self.gridLayout_6 = QGridLayout(self.headerContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_11 = QFrame(self.headerContainer)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_6.addWidget(self.frame_11, 0, 4, 1, 1)

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
        icon = QIcon()
        icon.addFile(u":/Icon_web/Image_for_main/icons_from_Web/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon)
        self.notificationBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_10)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        icon1 = QIcon()
        icon1.addFile(u":/Icon_web/Image_for_main/icons_from_Web/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon1)
        self.moreMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn, 0, Qt.AlignRight)

        self.profileMenuBtn = QPushButton(self.frame_10)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        icon2 = QIcon()
        icon2.addFile(u":/Icon_web/Image_for_main/icons_from_Web/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon2)
        self.profileMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn, 0, Qt.AlignRight)


        self.gridLayout_6.addWidget(self.frame_10, 0, 2, 1, 1)

        self.frame_9 = QFrame(self.headerContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(40, 40))
        self.label_13.setPixmap(QPixmap(u":/Icon_custom/Image_for_main/icon_custom/pharmacy.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_14.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainbodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setMinimumSize(QSize(574, 321))
        self.mainBodyContent.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainContentsContatiner = QWidget(self.mainBodyContent)
        self.mainContentsContatiner.setObjectName(u"mainContentsContatiner")
        self.mainContentsContatiner.setMinimumSize(QSize(0, 0))
        self.gridLayout_18 = QGridLayout(self.mainContentsContatiner)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(5, 5, 5, 0)
        self.mainPages = QStackedWidget(self.mainContentsContatiner)
        self.mainPages.setObjectName(u"mainPages")
        self.mainPages.setMinimumSize(QSize(0, 0))
        self.mainPages.setStyleSheet(u"QWidget#Search_Par {\n"
"    background-color: white;\n"
"    border: 1px solid rgb(28, 171, 213);\n"
"	color : black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_77 {\n"
"    margin: 0px; /* Adjust margin as needed */\n"
"}\n"
"\n"
"QLineEdit#lineEdit_9 {\n"
"    border: none;\n"
"    font-size: 10pt;\n"
"    padding: 5px;\n"
"	color : black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#pushButton_23 {\n"
"    background-color: rgb(28, 171, 213);;\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton#pushButton_23:hover {\n"
"    background-color: rgba(18, 163, 176, 0.8); /* Adjust opacity to your preference */\n"
"}\n"
"\n"
"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.gridLayout_19 = QGridLayout(self.homePage)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Search_Par = QWidget(self.homePage)
        self.Search_Par.setObjectName(u"Search_Par")
        self.Search_Par.setMinimumSize(QSize(0, 30))
        self.Search_Par.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.Search_Par)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 2, 5, 2)
        self.label_77 = QLabel(self.Search_Par)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMaximumSize(QSize(40, 32))
        self.label_77.setPixmap(QPixmap(u":/Icon_web/Image_for_main/icons_from_Web/search.svg"))

        self.horizontalLayout_5.addWidget(self.label_77)

        self.lineEdit_9 = QLineEdit(self.Search_Par)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEdit_9)

        self.pushButton_23 = QPushButton(self.Search_Par)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_23.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.pushButton_23)


        self.gridLayout_19.addWidget(self.Search_Par, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.homePage)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.widget_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* Styling for QScrollArea */\n"
"QScrollArea {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"    border: 1px solid rgb(28, 171, 213); /* Border color */\n"
"    border-radius: 10px; /* Border radius */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Styling for QScrollBar */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(28, 171, 213); /* Color of the scrollbar handle */\n"
"    border-radius: 5px; /* Handle border radius */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #bbb; /* Color of the scrollbar handle on hover */\n"
"}\n"
"\n"
"\n"
"/* Styling for QScrollBar arrows */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* Styling for QScrollBar page up and page "
                        "down */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Styling for QFrame inside QScrollArea (cards) */\n"
"QScrollArea QFrame {\n"
"    background-color: rgb(28, 171, 213); /* Updated card background color */\n"
"    border: 1px solid rgb(28, 171, 213); /* Card border color */\n"
"    border-radius: 10px; /* Card border radius */\n"
"}\n"
"\n"
"/* Styling for QCheckBox inside the Card */\n"
"QScrollArea QFrame QCheckBox {\n"
"    color: #000000; /* Checkbox text color */\n"
"}\n"
"\n"
"QScrollArea QFrame QPushButton {\n"
"   background-image:url(:/Icon_custom/Image_for_main/icon_custom/white_heart.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Hover effect for QPushButton */\n"
"QScrollArea QFrame QPushButton:hover {\n"
"   background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);\n"
"  background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Styling fo"
                        "r QLabel inside the Card */\n"
"QScrollArea QFrame QLabel {\n"
"    color: #ffff; /* Label text color */\n"
"    font-size: 12px; /* Font size */\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 581, 433))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_12 = QWidget(self.scrollAreaWidgetContents)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(230, 155))

        self.gridLayout_8.addWidget(self.widget_12, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.widget_7, 1, 0, 1, 1)

        self.Add_Frame = QFrame(self.homePage)
        self.Add_Frame.setObjectName(u"Add_Frame")
        self.Add_Frame.setMinimumSize(QSize(50, 35))
        self.Add_Frame.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* Button background color */\n"
"    color: black; /* Button text color */\n"
"    border: 1.5px solid #064666; /* No border */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #064666; /* Button background color on hover */\n"
"    color: black; /* Button text color on hover */\n"
"}\n"
"\n"
"")
        self.Add_Frame.setFrameShape(QFrame.StyledPanel)
        self.Add_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Add_Frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 20, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.pushButton_13 = QPushButton(self.Add_Frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(160, 25))
        self.pushButton_13.setMaximumSize(QSize(200, 16777215))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.pushButton_13.setFont(font6)

        self.horizontalLayout_8.addWidget(self.pushButton_13)


        self.gridLayout_19.addWidget(self.Add_Frame, 2, 0, 1, 1)

        self.mainPages.addWidget(self.homePage)
        self.orderPage = QWidget()
        self.orderPage.setObjectName(u"orderPage")
        self.orderPage.setStyleSheet(u"*{\n"
"color : black ;\n"
"}\n"
"#frame_15 {\n"
" 	margin-left:6px;\n"
"    border: 1px solid   #064666;\n"
"    border-top-right-radius: 15px;\n"
"    border-top-left-radius: 15px;\n"
"	\n"
"\n"
"}\n"
"#scrollArea_3 {\n"
"    border: 1px solid   #064666;\n"
"    border-bottom-right-radius: 15px;\n"
"    border-bottom-left-radius: 15px;\n"
"}\n"
"\n"
"#widget_9{\n"
"	border: 1px solid  #064666;\n"
"    border-bottom: 0px solid   rgb(7, 86, 126);\n"
"}")
        self.gridLayout_17 = QGridLayout(self.orderPage)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_15 = QFrame(self.orderPage)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 102))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setPixmap(QPixmap(u":/Icon_custom/Image_for_main/icon_custom/pngegg (1).png"))

        self.horizontalLayout_11.addWidget(self.label_26)

        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 81))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(1)
        self.gridLayout_9.setVerticalSpacing(15)
        self.label_27 = QLabel(self.frame_12)
        self.label_27.setObjectName(u"label_27")
        font7 = QFont()
        font7.setFamilies([u"MS Reference Sans Serif"])
        font7.setPointSize(10)
        self.label_27.setFont(font7)

        self.gridLayout_9.addWidget(self.label_27, 0, 1, 1, 1)

        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font7)

        self.gridLayout_9.addWidget(self.label_23, 1, 4, 1, 1)

        self.Patient_name_lineEdit_2 = QLineEdit(self.frame_12)
        self.Patient_name_lineEdit_2.setObjectName(u"Patient_name_lineEdit_2")
        font8 = QFont()
        font8.setPointSize(9)
        self.Patient_name_lineEdit_2.setFont(font8)

        self.gridLayout_9.addWidget(self.Patient_name_lineEdit_2, 3, 6, 1, 1)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)

        self.gridLayout_9.addWidget(self.label_25, 3, 1, 1, 1)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.gridLayout_9.addWidget(self.label_15, 1, 1, 1, 1)

        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(100, 0))
        self.label_31.setFont(font8)

        self.gridLayout_9.addWidget(self.label_31, 0, 2, 1, 1)

        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font8)

        self.gridLayout_9.addWidget(self.label_28, 1, 2, 1, 1)

        self.Patient_name_lineEdit = QLineEdit(self.frame_12)
        self.Patient_name_lineEdit.setObjectName(u"Patient_name_lineEdit")
        self.Patient_name_lineEdit.setFont(font8)

        self.gridLayout_9.addWidget(self.Patient_name_lineEdit, 1, 6, 1, 1)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font8)

        self.gridLayout_9.addWidget(self.label_29, 3, 2, 1, 1)

        self.label_32 = QLabel(self.frame_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))
        self.label_32.setFont(font8)

        self.gridLayout_9.addWidget(self.label_32, 0, 6, 1, 1)

        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font7)

        self.gridLayout_9.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font7)

        self.gridLayout_9.addWidget(self.label_30, 3, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_12)


        self.gridLayout_17.addWidget(self.frame_15, 0, 0, 1, 2)

        self.widget_8 = QWidget(self.orderPage)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_18 = QVBoxLayout(self.widget_8)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(6, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 25))
        self.widget_9.setStyleSheet(u"QLabel {\n"
"    border-right: 1px solid   #064666;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 0, 0, 0)
        self.Medicine_name = QLabel(self.widget_9)
        self.Medicine_name.setObjectName(u"Medicine_name")
        self.Medicine_name.setMinimumSize(QSize(220, 0))
        self.Medicine_name.setFont(font8)
        self.Medicine_name.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.Medicine_name)

        self.Count = QLabel(self.widget_9)
        self.Count.setObjectName(u"Count")
        self.Count.setMinimumSize(QSize(210, 0))
        self.Count.setMaximumSize(QSize(200, 16777215))
        self.Count.setFont(font8)
        self.Count.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.Count)

        self.Medicine_usage = QLabel(self.widget_9)
        self.Medicine_usage.setObjectName(u"Medicine_usage")
        self.Medicine_usage.setMinimumSize(QSize(50, 0))
        self.Medicine_usage.setMaximumSize(QSize(16777215, 16777215))
        self.Medicine_usage.setFont(font8)

        self.horizontalLayout_15.addWidget(self.Medicine_usage)

        self.Price = QLabel(self.widget_9)
        self.Price.setObjectName(u"Price")
        self.Price.setMinimumSize(QSize(50, 0))
        self.Price.setMaximumSize(QSize(16777215, 16777215))
        self.Price.setFont(font8)

        self.horizontalLayout_15.addWidget(self.Price)

        self.Edite = QLabel(self.widget_9)
        self.Edite.setObjectName(u"Edite")
        self.Edite.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.Edite)

        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(18, 16777215))

        self.horizontalLayout_15.addWidget(self.widget_10)


        self.verticalLayout_18.addWidget(self.widget_9)

        self.scrollArea_3 = QScrollArea(self.widget_8)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy2)
        self.scrollArea_3.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_3.setStyleSheet(u"QLabel,QLineEdit{\n"
"    border-left: 1px solid #064666;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"	border-righte:0px solid #064666;\n"
"    border-top:1px solid #064666;\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
" \n"
"    background-color: rgb(255, 34, 34);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"*{\n"
"border-bottom:1px solid #064666;\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.scrollArea_3.setFrameShape(QFrame.WinPanel)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 579, 318))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_16 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 35))
        self.frame_16.setMaximumSize(QSize(16777215, 35))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_16)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.frame_16)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 35))
        self.widget_13.setMaximumSize(QSize(16777215, 35))
        font9 = QFont()
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.widget_13.setFont(font9)
        self.widget_13.setStyleSheet(u"")
        self._2 = QHBoxLayout(self.widget_13)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.Medicine_name_4 = QLabel(self.widget_13)
        self.Medicine_name_4.setObjectName(u"Medicine_name_4")
        self.Medicine_name_4.setMinimumSize(QSize(210, 0))
        self.Medicine_name_4.setFont(font8)
        self.Medicine_name_4.setLayoutDirection(Qt.LeftToRight)

        self._2.addWidget(self.Medicine_name_4)

        self.lineEdit_11 = QLineEdit(self.widget_13)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 35))
        self.lineEdit_11.setMaximumSize(QSize(120, 35))
        self.lineEdit_11.setFont(font)

        self._2.addWidget(self.lineEdit_11)

        self.Medicine_usage_4 = QLabel(self.widget_13)
        self.Medicine_usage_4.setObjectName(u"Medicine_usage_4")
        self.Medicine_usage_4.setMinimumSize(QSize(50, 0))
        self.Medicine_usage_4.setFont(font8)

        self._2.addWidget(self.Medicine_usage_4)

        self.Price_4 = QLabel(self.widget_13)
        self.Price_4.setObjectName(u"Price_4")
        self.Price_4.setMinimumSize(QSize(50, 0))
        self.Price_4.setMaximumSize(QSize(150, 16777215))
        self.Price_4.setFont(font8)

        self._2.addWidget(self.Price_4)

        self.widget_delet_2 = QWidget(self.widget_13)
        self.widget_delet_2.setObjectName(u"widget_delet_2")
        self.widget_delet_2.setMinimumSize(QSize(35, 0))
        self.widget_delet_2.setMaximumSize(QSize(40, 16777215))
        self.widget_delet_2.setStyleSheet(u"*{\n"
"border:  1px solid #064666;\n"
"margine : 2px;}")
        self.verticalLayout_27 = QVBoxLayout(self.widget_delet_2)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.pushButton_Trash_2 = QPushButton(self.widget_delet_2)
        self.pushButton_Trash_2.setObjectName(u"pushButton_Trash_2")
        self.pushButton_Trash_2.setMaximumSize(QSize(35, 30))
        icon3 = QIcon()
        icon3.addFile(u":/Icon_web/Image_for_main/icons_from_Web/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Trash_2.setIcon(icon3)
        self.pushButton_Trash_2.setIconSize(QSize(14, 14))

        self.verticalLayout_27.addWidget(self.pushButton_Trash_2)


        self._2.addWidget(self.widget_delet_2)


        self.verticalLayout_20.addWidget(self.widget_13)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_18.addWidget(self.scrollArea_3)


        self.gridLayout_17.addWidget(self.widget_8, 1, 0, 1, 2)

        self.Print_Frame = QFrame(self.orderPage)
        self.Print_Frame.setObjectName(u"Print_Frame")
        self.Print_Frame.setMinimumSize(QSize(50, 35))
        self.Print_Frame.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* Button background color */\n"
"    color: black; /* Button text color */\n"
"    border: 1.5px solid #064666; /* No border */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #064666; /* Button background color on hover */\n"
"    color: black; /* Button text color on hover */\n"
"}\n"
"\n"
"")
        self.Print_Frame.setFrameShape(QFrame.StyledPanel)
        self.Print_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Print_Frame)
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 20, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.Print_button = QPushButton(self.Print_Frame)
        self.Print_button.setObjectName(u"Print_button")
        self.Print_button.setMinimumSize(QSize(150, 25))
        self.Print_button.setFont(font6)
        icon4 = QIcon()
        icon4.addFile(u":/Icon_web/Image_for_main/icons_from_Web/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Print_button.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.Print_button)


        self.gridLayout_17.addWidget(self.Print_Frame, 4, 1, 1, 1)

        self.mainPages.addWidget(self.orderPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_19 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_17 = QLabel(self.reportsPage)
        self.label_17.setObjectName(u"label_17")
        font10 = QFont()
        font10.setPointSize(13)
        self.label_17.setFont(font10)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_17)

        self.mainPages.addWidget(self.reportsPage)

        self.gridLayout_18.addWidget(self.mainPages, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mainContentsContatiner)

        self.rightMenuSubContainer = QWidget(self.mainBodyContent)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuSubContainer.setMaximumSize(QSize(215, 16777215))
        self.rightMenuSubContainer.setStyleSheet(u"#rightMenuSubContainer {\n"
"    border-radius: 10px;\n"
"}\n"
"#rightMenuPages{\n"
" background-color: white;\n"
"  border-radius: 7px;\n"
"}\n"
"/* Styling for QScrollArea */\n"
"QScrollArea {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"    border: 1.5px solid   #064666; /* Border color */\n"
"border-bottom-right-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"border-top-right-radius: 0;\n"
"border-top-left-radius: 0;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Styling for QScrollBar */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 10px; /* Width of the scrollbar */\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background:  rgb(28, 171, 213); /* Color of the scrollbar handle */\n"
"    border-radius: 5px; /* Handle border radius */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #bbb; /* Color of the scrollbar handle on hover */\n"
"}\n"
"\n"
"\n"
"/* Styling for QScrollBar arro"
                        "ws */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"\n"
"/* Styling for QScrollBar page up and page down */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Styling for QFrame inside QScrollArea (cards) */\n"
"QScrollArea QFrame {\n"
"    background-color: rgb(28, 171, 213); /* Updated card background color */\n"
"    border: 1px solid rgb(28, 171, 213); /* Card border color */\n"
"    border-radius: 10px; /* Card border radius */\n"
"}\n"
"\n"
"/* Styling for QCheckBox inside the Card */\n"
"QScrollArea QFrame QCheckBox {\n"
"    color: #000000; /* Checkbox text color */\n"
"}\n"
"\n"
"QScrollArea QFrame QPushButton {\n"
"   background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);\n"
"\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Hover effect for QPushBut"
                        "ton */\n"
"QScrollArea QFrame QPushButton:hover {\n"
"   background-image:url(:/Icon_custom/Image_for_main/icon_custom/white_heart.png);\n"
"  background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"/* Styling for QLabel inside the Card */\n"
"QScrollArea QFrame QLabel {\n"
"    color: #ffff; /* Label text color */\n"
"    font-size: 11px; /* Font size */\n"
"}\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.frame_13 = QFrame(self.rightMenuSubContainer)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_18)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.rightMenuPages = QStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_22 = QVBoxLayout(self.profilePage)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_19 = QLabel(self.profilePage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font10)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_19)

        self.rightMenuPages.addWidget(self.profilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_23 = QVBoxLayout(self.morePage)
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.morePage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 205, 497))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_23.addWidget(self.scrollArea_2)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_21.addWidget(self.rightMenuPages)


        self.horizontalLayout.addWidget(self.rightMenuSubContainer)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 2)

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
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(True)
        self.label_21.setFont(font11)

        self.verticalLayout_25.addWidget(self.label_21)

        self.frame_14 = QFrame(self.popupNotificationSubContainer)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font12 = QFont()
        font12.setBold(False)
        self.label_22.setFont(font12)
        self.label_22.setStyleSheet(u"")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)


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

        self.leftMenuContainer = QWidget(self.frame_4)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(101, 16777215))
        self.leftMenuContainer.setStyleSheet(u"/* Styling for QPushButton */\n"
"QPushButton {\n"
"    background-color:transparent; /* Default background color */\n"
"    color: #fff; /* Text color */\n"
" 	border: 1px solid transparent ;\n"
"    padding: 1px 2px; /* Padding */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Styling for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color:rgb(28, 171, 213);; /* Background color on hover */\n"
"\n"
"}\n"
"\n"
"/* Styling for QFrame (the container) */\n"
"QFrame {\n"
"    background-color: transparent; /* Transparent background */\n"
"     /* No border */\n"
"	padding : 2px;\n"
"}\n"
"QPushButton::icon {\n"
"    color: white; /* or any other color you want for the icon */\n"
"}\n"
"*{\n"
"background-color :rgb(2, 32, 47) ;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setMinimumSize(QSize(30, 0))
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
        self.menuBtn.setStyleSheet(u"*{\n"
"padding-top: 5px;\n"
"margin-top : 6px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icon_web/Image_for_main/icons_from_Web/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon5)
        self.menuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_13.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.leftMenuSubContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_7)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(19, 0))
        self.homeBtn.setMaximumSize(QSize(101, 16777215))
        self.homeBtn.setAutoFillBackground(False)
        self.homeBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Icon_web/Image_for_main/icons_from_Web/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon6)
        self.homeBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.homeBtn)

        self.orderBtn = QPushButton(self.frame_7)
        self.orderBtn.setObjectName(u"orderBtn")
        self.orderBtn.setMinimumSize(QSize(19, 0))
        self.orderBtn.setMaximumSize(QSize(101, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Icon_web/Image_for_main/icons_from_Web/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderBtn.setIcon(icon7)
        self.orderBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.orderBtn)

        self.reportsBtn = QPushButton(self.frame_7)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setMinimumSize(QSize(19, 0))
        self.reportsBtn.setMaximumSize(QSize(101, 16777215))
        self.reportsBtn.setIcon(icon4)
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
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_8)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(19, 0))
        self.settingsBtn.setMaximumSize(QSize(101, 16777215))
        icon8 = QIcon()
        icon8.addFile(u":/Icon_web/Image_for_main/icons_from_Web/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon8)
        self.settingsBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_8)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(19, 0))
        self.infoBtn.setMaximumSize(QSize(101, 16777215))
        icon9 = QIcon()
        icon9.addFile(u":/Icon_web/Image_for_main/icons_from_Web/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon9)
        self.infoBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_8)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(19, 0))
        self.helpBtn.setMaximumSize(QSize(101, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/Icon_web/Image_for_main/icons_from_Web/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon10)
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
        self.frame_5.setStyleSheet(u"/* Styling for QPushButton */\n"
"QPushButton {\n"
"    background-color:transparent; /* Default background color */\n"
"    color: black; /* Text color */\n"
" 	border: 1px solid black ;\n"
"    padding: 1px 2px; /* Padding */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Styling for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: rgb(18, 163, 176); /* Background color on hover */\n"
"\n"
"}\n"
"\n"
"/* Styling for QFrame (the container) */\n"
"QFrame {\n"
"    background-color: transparent; /* Transparent background */\n"
"     /* No border */\n"
"	padding : 2px;\n"
"}\n"
"")
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
        self.label_7.setFont(font10)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.centerMenuPages.addWidget(self.settingPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.helpPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font10)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8)

        self.centerMenuPages.addWidget(self.helpPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_11 = QVBoxLayout(self.infoPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.Home_Frame = QFrame(self.infoPage)
        self.Home_Frame.setObjectName(u"Home_Frame")
        self.Home_Frame.setFrameShape(QFrame.StyledPanel)
        self.Home_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.Home_Frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(15)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.widget_6 = QWidget(self.Home_Frame)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout_7.addWidget(self.widget_6, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.Home_Frame)

        self.label_12 = QLabel(self.infoPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font10)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.centerMenuPages.addWidget(self.infoPage)

        self.verticalLayout_8.addWidget(self.centerMenuPages)


        self.verticalLayout_7.addWidget(self.centerMenuSubContainer)


        self.gridLayout_5.addWidget(self.centerMenuContatiner, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.Main_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)
        self.centerMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email@example.com", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Welcome To Smart Pharmacy App", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Not Registerd ? Register ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.ErrorMessage_2.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter you Information below", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email@example.com", None))
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
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Smart Pharmacy", None))
        self.label_77.setText("")
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write medicin name", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"ADD to Prescription", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Dr Name :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Patient Name :", None))
        self.Patient_name_lineEdit_2.setText("")
        self.Patient_name_lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter patient age", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Date      :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Dr Depart :", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.Patient_name_lineEdit.setText("")
        self.Patient_name_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter patient name", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy ", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Per Number", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Prescription ID : ", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Patient Age :", None))
        self.Medicine_name.setText(QCoreApplication.translate("MainWindow", u"Medicine Name ", None))
        self.Count.setText(QCoreApplication.translate("MainWindow", u" Medicine Usage", None))
        self.Medicine_usage.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.Price.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.Edite.setText(QCoreApplication.translate("MainWindow", u"Edite", None))
        self.Medicine_name_4.setText(QCoreApplication.translate("MainWindow", u"Medicine Name ", None))
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u" Medicine Usage", None))
        self.Medicine_usage_4.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.Price_4.setText(QCoreApplication.translate("MainWindow", u"Count", None))
        self.pushButton_Trash_2.setText("")
        self.Print_button.setText(QCoreApplication.translate("MainWindow", u" Print", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Favorite List", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Notifications Message", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u" Menu", None))
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
#if QT_CONFIG(tooltip)
        self.orderBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Order", None))
#endif // QT_CONFIG(tooltip)
        self.orderBtn.setText(QCoreApplication.translate("MainWindow", u"  Prescription", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u" Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Informations", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u" Informations", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"   Help", None))
#if QT_CONFIG(statustip)
        self.centerMenuContatiner.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Informations", None))
    # retranslateUi

