# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pharm_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

import Final_Main_ph_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1283, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setToolTipDuration(-1)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(0)
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.Main_page.setStyleSheet(u"* {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget {\n"
"    background-color: #b7e1a1; \n"
"}\n"
"\n"
"#leftMenuSubContainer {\n"
"    background-color: #b7e1a1; \n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton {\n"
"    text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer {\n"
"    background-color: #b7e1a1; /* Dark green */\n"
"}\n"
"\n"
"#popupNotificationSubContainer {\n"
"    background-color: #b7e1a1; \n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#headerContainer, #footerContainer {\n"
"    background-color: #b7e1a1; \n"
"}\n"
"\n"
"#frame_4, #frame_8 {\n"
"    background-color: #FFFF; /* Light green */\n"
"    border-radius: 10px;\n"
"}\n"
"#frame_11{\n"
"    background-color: #265c36; \n"
"}\n"
"#leftMenuContainer {\n"
"    padding-top"
                        ": 20px;\n"
"}\n"
"")
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
"    background-color: #265c36; \n"
"}")
        self.gridLayout_6 = QGridLayout(self.headerContainer)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
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
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label_14.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_14)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)

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

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.verticalLayout_16.addWidget(self.headerContainer)

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
"    border: 1px solid rgb(183, 225, 161);\n"
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
"	    padding: 5px;\n"
"	color : black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#pushButton_23 {\n"
"    background-color: #b7e1a1;\n"
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
"QWidget#widget_12 {\n"
"    background-color: white;\n"
"    border right: 1px solid rgb(183, 225, 161);\n"
"    border : 1px solid rgb(183, 225, 161);\n"
"	color : black;\n"
"\n"
"}\n"
"\n"
"\n"
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
        self.label_77.setPixmap(QPixmap(u":/Icon_custom/Image_for_main/icon_custom/prescription.png"))

        self.horizontalLayout_5.addWidget(self.label_77)

        self.lineEdit_9 = QLineEdit(self.Search_Par)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit_9.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lineEdit_9)

        self.pushButton_23 = QPushButton(self.Search_Par)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_23.setStyleSheet(u"#pushButton_23{\n"
"    background-color: #265c36; \n"
"}")
        self.pushButton_23.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.pushButton_23)


        self.gridLayout_19.addWidget(self.Search_Par, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.homePage)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.widget_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_12 = QWidget(self.frame_3)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_32 = QVBoxLayout(self.widget_12)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(6, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_12)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 25))
        self.widget_17.setStyleSheet(u"QLabel , QLineEdit {\n"
"   border-left: 1px solid #1fc150;\n"
"   border-top: 0.8px solid #1fc150;\n"
"   border-right: 1px solid #1fc150;\n"
"   border-bottom: 0.8px solid #1fc150;\n"
"	color:black;\n"
"   qproperty-alignment: 'AlignCenter'\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_8 = QGridLayout(self.widget_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Date = QLabel(self.widget_17)
        self.Date.setObjectName(u"Date")
        self.Date.setLineWidth(2)

        self.gridLayout_8.addWidget(self.Date, 0, 3, 1, 1)

        self.Medicine_name_5 = QLabel(self.widget_17)
        self.Medicine_name_5.setObjectName(u"Medicine_name_5")
        self.Medicine_name_5.setMinimumSize(QSize(220, 0))
        font2 = QFont()
        font2.setPointSize(9)
        self.Medicine_name_5.setFont(font2)
        self.Medicine_name_5.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_8.addWidget(self.Medicine_name_5, 1, 0, 1, 1)

        self.Count_3 = QLabel(self.widget_17)
        self.Count_3.setObjectName(u"Count_3")
        self.Count_3.setMinimumSize(QSize(50, 0))
        self.Count_3.setMaximumSize(QSize(200, 16777215))
        self.Count_3.setFont(font2)
        self.Count_3.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_8.addWidget(self.Count_3, 1, 3, 1, 1)

        self.Doctor_Name = QLabel(self.widget_17)
        self.Doctor_Name.setObjectName(u"Doctor_Name")

        self.gridLayout_8.addWidget(self.Doctor_Name, 0, 0, 1, 1)

        self.Edite_3 = QLabel(self.widget_17)
        self.Edite_3.setObjectName(u"Edite_3")
        self.Edite_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_8.addWidget(self.Edite_3, 1, 4, 1, 1)

        self.Price_5 = QLabel(self.widget_17)
        self.Price_5.setObjectName(u"Price_5")
        self.Price_5.setMinimumSize(QSize(50, 0))
        self.Price_5.setMaximumSize(QSize(16777215, 16777215))
        self.Price_5.setFont(font2)

        self.gridLayout_8.addWidget(self.Price_5, 1, 2, 1, 1)

        self.Medicine_usage_5 = QLabel(self.widget_17)
        self.Medicine_usage_5.setObjectName(u"Medicine_usage_5")
        self.Medicine_usage_5.setMinimumSize(QSize(210, 0))
        self.Medicine_usage_5.setMaximumSize(QSize(16777215, 16777215))
        self.Medicine_usage_5.setFont(font2)

        self.gridLayout_8.addWidget(self.Medicine_usage_5, 1, 1, 1, 1)


        self.verticalLayout_32.addWidget(self.widget_17)

        self.scrollArea_6 = QScrollArea(self.widget_12)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_6.sizePolicy().hasHeightForWidth())
        self.scrollArea_6.setSizePolicy(sizePolicy2)
        self.scrollArea_6.setMinimumSize(QSize(0, 0))
        self.scrollArea_6.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_6.setStyleSheet(u"")
        self.scrollArea_6.setFrameShape(QFrame.WinPanel)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 689, 279))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_32.addWidget(self.scrollArea_6)


        self.verticalLayout.addWidget(self.widget_12)


        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 1)


        self.gridLayout_19.addWidget(self.widget_7, 1, 0, 1, 1)

        self.Add_Frame = QFrame(self.homePage)
        self.Add_Frame.setObjectName(u"Add_Frame")
        self.Add_Frame.setMinimumSize(QSize(50, 35))
        self.Add_Frame.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* Button background color */\n"
"    color: black; /* Button text color */\n"
"    border: 1.5px solid  rgb(29, 170, 97); /* Border color */; /* No border */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: border: 1px solid rgb(29, 170, 97); /* Border color */; /* Button background color on hover */\n"
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

        self.ADD_To_Machine = QPushButton(self.Add_Frame)
        self.ADD_To_Machine.setObjectName(u"ADD_To_Machine")
        self.ADD_To_Machine.setMinimumSize(QSize(160, 25))
        self.ADD_To_Machine.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.ADD_To_Machine.setFont(font3)

        self.horizontalLayout_8.addWidget(self.ADD_To_Machine)


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
        self.frame_12 = QFrame(self.orderPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_19 = QFrame(self.frame_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_19)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 30))
        self.frame_20.setMaximumSize(QSize(16777215, 32))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Search_Par_3 = QWidget(self.frame_20)
        self.Search_Par_3.setObjectName(u"Search_Par_3")
        self.Search_Par_3.setMinimumSize(QSize(300, 30))
        self.Search_Par_3.setMaximumSize(QSize(16777215, 32))
        self.Search_Par_3.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"    border: 1px solid  rgb(29, 170, 97);\n"
"	color : black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    margin: 0px; /* Adjust margin as needed */\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    font-size: 10pt;\n"
"    padding: 5px;\n"
"	color : black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:  rgb(29, 170, 97);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:  rgb(29, 170, 97); /* Button background color */\n"
"    color: White; /* Button text color */\n"
"    border: 1.2px solid  rgb(29, 170, 97); /* Border color */; /* No border */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: border: 1px solid rgb(29, 170, 97); /* Border color */; /* Button background color"
                        " on hover */\n"
"    color: black; /* Button text color on hover */\n"
"}\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.Search_Par_3)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 2, 6, 2)
        self.label_79 = QLabel(self.Search_Par_3)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMaximumSize(QSize(25, 20))
        self.label_79.setPixmap(QPixmap(u":/Icon_web/Image_for_main/icons_from_Web/search.svg"))

        self.horizontalLayout_14.addWidget(self.label_79)

        self.lineEdit_12 = QLineEdit(self.Search_Par_3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font1)

        self.horizontalLayout_14.addWidget(self.lineEdit_12)

        self.pushButton_25 = QPushButton(self.Search_Par_3)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMaximumSize(QSize(16777215, 22))
        self.pushButton_25.setIconSize(QSize(15, 15))

        self.horizontalLayout_14.addWidget(self.pushButton_25)


        self.horizontalLayout_18.addWidget(self.Search_Par_3)


        self.gridLayout_16.addWidget(self.frame_20, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.frame_19)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_11 = QGridLayout(self.widget_14)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_5 = QScrollArea(self.widget_14)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"/* Styling for QScrollArea */\n"
"QScrollArea {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"     border: 1.2px solid  rgb(29, 170, 97); /* Border color */\n"
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
"    background:  rgb(29, 170, 97); /* Color of the scrollbar handle */\n"
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
"/* Styling for QScrollBar page up and pa"
                        "ge down */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Styling for QFrame inside QScrollArea (cards) */\n"
"QScrollArea QFrame {\n"
"	 background: white;\n"
"   color:balck;\n"
"    border: 1.2px solid   rgb(29, 170, 97); /* Card border color */\n"
"    border-radius: 10px; /* Card border radius */\n"
"}\n"
"\n"
"/* Styling for QCheckBox inside the Card */\n"
"QScrollArea QFrame QCheckBox {\n"
"    color: #000000; /* Checkbox text color */\n"
"}\n"
"\n"
"\n"
"\n"
"/* Styling for QLabel inside the Card */\n"
"QScrollArea QFrame QLabel {\n"
"    color: #ffff; /* Label text color */\n"
"    font-size: 12px; /* Font size */\n"
"	border: 0px solid rgb(28, 171, 213); \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: 005c4b; /* Button background color */\n"
"    color: white; /* Button text color */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background-color:#005c4b;\n"
""
                        "}\n"
"\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 671, 357))
        self.gridLayout_13 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_5)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Cared_13 = QFrame(self.widget_3)
        self.Cared_13.setObjectName(u"Cared_13")
        self.Cared_13.setMinimumSize(QSize(200, 100))
        self.Cared_13.setMaximumSize(QSize(200, 110))
        self.Cared_13.setAutoFillBackground(False)
        self.Cared_13.setStyleSheet(u"#pushButton_8{\n"
"    background-color: #265c36; \n"
"}")
        self.Cared_13.setFrameShape(QFrame.StyledPanel)
        self.Cared_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.Cared_13)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_73 = QLabel(self.Cared_13)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(110, 0))

        self.gridLayout_15.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.Cared_13)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_15.addWidget(self.label_74, 2, 0, 1, 1)

        self.label_75 = QLabel(self.Cared_13)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_15.addWidget(self.label_75, 1, 0, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_15, 1, 0, 3, 1)

        self.label_43 = QLabel(self.Cared_13)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_14.addWidget(self.label_43, 2, 1, 1, 1)

        self.label_41 = QLabel(self.Cared_13)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_14.addWidget(self.label_41, 1, 1, 1, 1)

        self.label_42 = QLabel(self.Cared_13)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_14.addWidget(self.label_42, 3, 1, 1, 1)

        self.checkBox = QCheckBox(self.Cared_13)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_14.addWidget(self.checkBox, 0, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.Cared_13)


        self.gridLayout_13.addWidget(self.widget_3, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_11.addWidget(self.scrollArea_5, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_14, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_19)


        self.gridLayout_17.addWidget(self.frame_12, 0, 0, 1, 1)

        self.mainPages.addWidget(self.orderPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.verticalLayout_19 = QVBoxLayout(self.reportsPage)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.frame_16 = QFrame(self.reportsPage)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 30))
        self.frame_17.setMaximumSize(QSize(16777215, 32))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Search_Par_2 = QWidget(self.frame_17)
        self.Search_Par_2.setObjectName(u"Search_Par_2")
        self.Search_Par_2.setMinimumSize(QSize(300, 30))
        self.Search_Par_2.setMaximumSize(QSize(16777215, 32))
        self.Search_Par_2.setStyleSheet(u"QWidget{\n"
"    background-color: white;\n"
"    border: 1px solid  rgb(29, 170, 97);\n"
"	color : black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"    margin: 0px; /* Adjust margin as needed */\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: none;\n"
"    font-size: 10pt;\n"
"    padding: 5px;\n"
"	color : black;\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:  rgb(29, 170, 97);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:  rgb(29, 170, 97); /* Button background color */\n"
"    color: White; /* Button text color */\n"
"    border: 1.2px solid  rgb(29, 170, 97); /* Border color */; /* No border */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: border: 1px solid rgb(29, 170, 97); /* Border color */; /* Button background color"
                        " on hover */\n"
"    color: black; /* Button text color on hover */\n"
"}\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.Search_Par_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 2, 6, 2)
        self.label_78 = QLabel(self.Search_Par_2)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMaximumSize(QSize(25, 20))
        self.label_78.setPixmap(QPixmap(u":/Icon_web/Image_for_main/icons_from_Web/search.svg"))

        self.horizontalLayout_13.addWidget(self.label_78)

        self.lineEdit_11 = QLineEdit(self.Search_Par_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font1)

        self.horizontalLayout_13.addWidget(self.lineEdit_11)

        self.pushButton_24 = QPushButton(self.Search_Par_2)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMaximumSize(QSize(16777215, 22))
        self.pushButton_24.setIconSize(QSize(15, 15))

        self.horizontalLayout_13.addWidget(self.pushButton_24)


        self.horizontalLayout_16.addWidget(self.Search_Par_2)


        self.verticalLayout_27.addWidget(self.frame_17)

        self.widget_13 = QWidget(self.frame_16)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_10 = QGridLayout(self.widget_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.widget_13)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"/* Styling for QScrollArea */\n"
"QScrollArea {\n"
"    background-color: #f0f0f0; /* Background color */\n"
"     border: 1.2px solid  rgb(29, 170, 97); /* Border color */\n"
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
"    background:  rgb(29, 170, 97); /* Color of the scrollbar handle */\n"
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
"/* Styling for QScrollBar page up and pa"
                        "ge down */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* Styling for QFrame inside QScrollArea (cards) */\n"
"QScrollArea QFrame {\n"
"	 background: white;\n"
"   color:balck;\n"
"    border: 1.2px solid   rgb(29, 170, 97); /* Card border color */\n"
"    border-radius: 10px; /* Card border radius */\n"
"}\n"
"\n"
"/* Styling for QCheckBox inside the Card */\n"
"QScrollArea QFrame QCheckBox {\n"
"    color: #000000; /* Checkbox text color */\n"
"}\n"
"\n"
"\n"
"\n"
"/* Styling for QLabel inside the Card */\n"
"QScrollArea QFrame QLabel {\n"
"    color: #ffff; /* Label text color */\n"
"    font-size: 12px; /* Font size */\n"
"	border: 0px solid rgb(28, 171, 213); \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: 005c4b; /* Button background color */\n"
"    color: white; /* Button text color */\n"
"    border-radius: 10px; /* Button border radius */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	 background-color:#005c4b;\n"
""
                        "}\n"
"\n"
"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 703, 389))
        self.gridLayout_12 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_20 = QGridLayout(self.widget_2)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.Cared_10 = QFrame(self.widget_2)
        self.Cared_10.setObjectName(u"Cared_10")
        self.Cared_10.setMinimumSize(QSize(0, 50))
        self.Cared_10.setMaximumSize(QSize(300, 95))
        self.Cared_10.setAutoFillBackground(False)
        self.Cared_10.setStyleSheet(u"#pushButton_8{\n"
"    background-color: #265c36; \n"
"}")
        self.Cared_10.setFrameShape(QFrame.StyledPanel)
        self.Cared_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.Cared_10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_46 = QLabel(self.Cared_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(110, 0))

        self.gridLayout_21.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_47 = QLabel(self.Cared_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(200, 0))

        self.gridLayout_21.addWidget(self.label_47, 0, 1, 1, 2)

        self.label_48 = QLabel(self.Cared_10)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_21.addWidget(self.label_48, 1, 0, 1, 1)

        self.label_37 = QLabel(self.Cared_10)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_21.addWidget(self.label_37, 1, 1, 1, 1)

        self.label_49 = QLabel(self.Cared_10)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_21.addWidget(self.label_49, 2, 0, 1, 1)

        self.label_45 = QLabel(self.Cared_10)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_21.addWidget(self.label_45, 2, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.Cared_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(70, 24))
        self.pushButton_8.setMaximumSize(QSize(50, 24))
        self.pushButton_8.setBaseSize(QSize(0, 0))
        self.pushButton_8.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/Icon_web/Image_for_main/icons_from_Web/external-link.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)

        self.gridLayout_21.addWidget(self.pushButton_8, 2, 2, 2, 1)

        self.label_50 = QLabel(self.Cared_10)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_21.addWidget(self.label_50, 3, 0, 1, 1)

        self.label_51 = QLabel(self.Cared_10)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_21.addWidget(self.label_51, 3, 1, 1, 1)


        self.gridLayout_20.addWidget(self.Cared_10, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_2, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_10.addWidget(self.scrollArea_4, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.widget_13)


        self.verticalLayout_19.addWidget(self.frame_16)

        self.mainPages.addWidget(self.reportsPage)
        self.AI = QWidget()
        self.AI.setObjectName(u"AI")
        self.mainPages.addWidget(self.AI)

        self.gridLayout_18.addWidget(self.mainPages, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mainContentsContatiner)

        self.rightMenuSubContainer = QWidget(self.mainBodyContent)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuSubContainer.setMaximumSize(QSize(215, 1000))
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
        self.label_18.setFont(font1)
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
        font4 = QFont()
        font4.setPointSize(13)
        self.label_19.setFont(font4)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 205, 345))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_23.addWidget(self.scrollArea_2)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_21.addWidget(self.rightMenuPages)

        self.frame_2 = QFrame(self.rightMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 70))
        self.frame_2.setMaximumSize(QSize(16777215, 16777210))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_2)


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
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_21.setFont(font5)

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
        font6 = QFont()
        font6.setBold(False)
        self.label_22.setFont(font6)
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
"    background-color: transparent; /* Default background color */\n"
"    color: #fff; /* Text color */\n"
"    border: 1px solid transparent;\n"
"    padding: 1px 2px; /* Padding */\n"
"    border-radius: 5px; /* Border radius */\n"
"}\n"
"\n"
"/* Styling for QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: rgb(28, 171, 213); /* Background color on hover */\n"
"}\n"
"\n"
"/* Styling for QFrame (the container) */\n"
"QFrame {\n"
"    background-color: transparent; /* Transparent background */\n"
"    /* No border */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"    color: white; /* or any other color you want for the icon */\n"
"}\n"
"\n"
"* {\n"
"    background-color: #265c36; /* Default green background color */\n"
"}\n"
"")
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
        icon4 = QIcon()
        icon4.addFile(u":/Icon_web/Image_for_main/icons_from_Web/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/Icon_web/Image_for_main/icons_from_Web/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon5)
        self.homeBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.homeBtn)

        self.orderBtn = QPushButton(self.frame_7)
        self.orderBtn.setObjectName(u"orderBtn")
        self.orderBtn.setMinimumSize(QSize(19, 0))
        self.orderBtn.setMaximumSize(QSize(101, 16777215))
        icon6 = QIcon()
        icon6.addFile(u":/Icon_web/Image_for_main/icons_from_Web/list.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.orderBtn.setIcon(icon6)
        self.orderBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.orderBtn)

        self.reportsBtn = QPushButton(self.frame_7)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setMinimumSize(QSize(19, 0))
        self.reportsBtn.setMaximumSize(QSize(101, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/Icon_web/Image_for_main/icons_from_Web/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportsBtn.setIcon(icon7)
        self.reportsBtn.setIconSize(QSize(20, 24))

        self.verticalLayout_14.addWidget(self.reportsBtn)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.pushButton = QPushButton(self.leftMenuSubContainer)
        self.pushButton.setObjectName(u"pushButton")
        icon8 = QIcon()
        icon8.addFile(u":/Icon_web/Image_for_main/icons_from_Web/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)

        self.verticalLayout_13.addWidget(self.pushButton)

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
        icon9 = QIcon()
        icon9.addFile(u":/Icon_web/Image_for_main/icons_from_Web/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon9)
        self.settingsBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_8)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setMinimumSize(QSize(19, 0))
        self.infoBtn.setMaximumSize(QSize(101, 16777215))
        icon10 = QIcon()
        icon10.addFile(u":/Icon_web/Image_for_main/icons_from_Web/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon10)
        self.infoBtn.setIconSize(QSize(16, 24))

        self.verticalLayout_15.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_8)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(19, 0))
        self.helpBtn.setMaximumSize(QSize(101, 16777215))
        icon11 = QIcon()
        icon11.addFile(u":/Icon_web/Image_for_main/icons_from_Web/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon11)
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
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.centerMenuPages.addWidget(self.settingPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_10 = QVBoxLayout(self.helpPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.helpPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
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
        self.label_12.setFont(font4)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.centerMenuPages.addWidget(self.infoPage)

        self.verticalLayout_8.addWidget(self.centerMenuPages)


        self.verticalLayout_7.addWidget(self.centerMenuSubContainer)


        self.gridLayout_5.addWidget(self.centerMenuContatiner, 0, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.Main_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(1)
        self.rightMenuPages.setCurrentIndex(1)
        self.centerMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.label_77.setText("")
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write Prescription ID", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.Date.setText(QCoreApplication.translate("MainWindow", u"   Date   ", None))
        self.Medicine_name_5.setText(QCoreApplication.translate("MainWindow", u"Medicine Name ", None))
#if QT_CONFIG(whatsthis)
        self.Count_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Count_3.setText(QCoreApplication.translate("MainWindow", u"    Count     ", None))
        self.Doctor_Name.setText(QCoreApplication.translate("MainWindow", u"DoctorName", None))
        self.Edite_3.setText(QCoreApplication.translate("MainWindow", u"   Edit   ", None))
        self.Price_5.setText(QCoreApplication.translate("MainWindow", u"    Price    ", None))
        self.Medicine_usage_5.setText(QCoreApplication.translate("MainWindow", u" Medicine Usage", None))
        self.ADD_To_Machine.setText(QCoreApplication.translate("MainWindow", u"ADD To Machine", None))
        self.label_79.setText("")
        self.lineEdit_12.setInputMask("")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write medicine name", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Search ", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"English Name:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Active Substance : ", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Price :", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_78.setText("")
        self.lineEdit_11.setInputMask("")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"write prescription Id or date", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Search ", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Prescription id :", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Doctor Name :", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Date & Time :", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Total Price : ", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"_________", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Receipt", None))
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
        self.orderBtn.setText(QCoreApplication.translate("MainWindow", u"Receipt Data", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u" Medicines", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"        AI", None))
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

