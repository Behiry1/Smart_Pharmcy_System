# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Prescription.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import Final_Main_ph_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(792, 1123)
        Form.setMinimumSize(QSize(792, 1123))
        Form.setMaximumSize(QSize(792, 1123))
        self.frame_15 = QFrame(Form)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 10, 781, 127))
        self.frame_15.setMinimumSize(QSize(0, 102))
        self.frame_15.setStyleSheet(u"*{\n"
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
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(10)
        self.label_27.setFont(font)

        self.gridLayout_9.addWidget(self.label_27, 0, 1, 1, 1)

        self.label_23 = QLabel(self.frame_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_9.addWidget(self.label_23, 1, 4, 1, 1)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_9.addWidget(self.label_25, 3, 1, 1, 1)

        self.label_15 = QLabel(self.frame_12)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_9.addWidget(self.label_15, 1, 1, 1, 1)

        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_31.setFont(font1)

        self.gridLayout_9.addWidget(self.label_31, 0, 2, 1, 1)

        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_9.addWidget(self.label_28, 1, 2, 1, 1)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_9.addWidget(self.label_29, 3, 2, 1, 1)

        self.label_32 = QLabel(self.frame_12)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))
        self.label_32.setFont(font1)

        self.gridLayout_9.addWidget(self.label_32, 0, 6, 1, 1)

        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_9.addWidget(self.label_24, 0, 4, 1, 1)

        self.label_30 = QLabel(self.frame_12)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)

        self.gridLayout_9.addWidget(self.label_30, 3, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.label = QLabel(self.frame_12)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 1, 5, 1, 2)

        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_9.addWidget(self.label_2, 3, 5, 1, 2)


        self.horizontalLayout_11.addWidget(self.frame_12)

        self.widget_8 = QWidget(Form)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 150, 781, 350))
        self.verticalLayout_19 = QVBoxLayout(self.widget_8)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(6, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 25))
        self.widget_12.setStyleSheet(u"QLabel {\n"
"    border-right: 1px solid   #064666;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 0, 0)
        self.Medicine_name_2 = QLabel(self.widget_12)
        self.Medicine_name_2.setObjectName(u"Medicine_name_2")
        self.Medicine_name_2.setMinimumSize(QSize(220, 0))
        self.Medicine_name_2.setFont(font1)
        self.Medicine_name_2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.Medicine_name_2)

        self.Medicine_usage_2 = QLabel(self.widget_12)
        self.Medicine_usage_2.setObjectName(u"Medicine_usage_2")
        self.Medicine_usage_2.setMinimumSize(QSize(210, 0))
        self.Medicine_usage_2.setMaximumSize(QSize(16777215, 16777215))
        self.Medicine_usage_2.setFont(font1)

        self.horizontalLayout_16.addWidget(self.Medicine_usage_2)

        self.Price_2 = QLabel(self.widget_12)
        self.Price_2.setObjectName(u"Price_2")
        self.Price_2.setMinimumSize(QSize(50, 0))
        self.Price_2.setMaximumSize(QSize(16777215, 16777215))
        self.Price_2.setFont(font1)

        self.horizontalLayout_16.addWidget(self.Price_2)

        self.Count_2 = QLabel(self.widget_12)
        self.Count_2.setObjectName(u"Count_2")
        self.Count_2.setMinimumSize(QSize(50, 0))
        self.Count_2.setMaximumSize(QSize(200, 16777215))
        self.Count_2.setFont(font1)
        self.Count_2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.Count_2)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(18, 16777215))

        self.horizontalLayout_16.addWidget(self.widget_13)


        self.verticalLayout_19.addWidget(self.widget_12)

        self.scrollArea_4 = QScrollArea(self.widget_8)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setFrameShape(QFrame.WinPanel)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 771, 321))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_14 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 30))
        self.widget_14.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.widget_14.setFont(font2)
        self.widget_14.setStyleSheet(u"QLabel , QLineEdit {\n"
"    border-left: 1px solid #064666;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"	border-righte:0px solid #064666;\n"
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
"border-top:1px solid #064666;\n"
"\n"
"}\n"
"\n"
"")
        self._2 = QHBoxLayout(self.widget_14)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.Medicine_name_4 = QLabel(self.widget_14)
        self.Medicine_name_4.setObjectName(u"Medicine_name_4")
        self.Medicine_name_4.setMinimumSize(QSize(220, 0))
        self.Medicine_name_4.setFont(font1)
        self.Medicine_name_4.setLayoutDirection(Qt.LeftToRight)

        self._2.addWidget(self.Medicine_name_4)

        self.Medicine_usage_4 = QLabel(self.widget_14)
        self.Medicine_usage_4.setObjectName(u"Medicine_usage_4")
        self.Medicine_usage_4.setMinimumSize(QSize(210, 0))
        self.Medicine_usage_4.setFont(font1)

        self._2.addWidget(self.Medicine_usage_4)

        self.Price_4 = QLabel(self.widget_14)
        self.Price_4.setObjectName(u"Price_4")
        self.Price_4.setMinimumSize(QSize(50, 0))
        self.Price_4.setMaximumSize(QSize(150, 16777215))
        self.Price_4.setFont(font1)

        self._2.addWidget(self.Price_4)

        self.lineEdit_11 = QLineEdit(self.widget_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(50, 0))
        self.lineEdit_11.setMaximumSize(QSize(50, 30))
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEdit_11.setFont(font3)

        self._2.addWidget(self.lineEdit_11)


        self.verticalLayout_21.addWidget(self.widget_14)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_19.addWidget(self.scrollArea_4)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 670, 731, 431))
        self.Total_Price_Label = QLabel(Form)
        self.Total_Price_Label.setObjectName(u"Total_Price_Label")
        self.Total_Price_Label.setGeometry(QRect(618, 530, 131, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("Form", u"Dr Name :", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Patient Name :", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Date      :", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Dr Depart :", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Department", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"dd/mm/yyyy ", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Per Number", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Prescription ID : ", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Patient Age :", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Age", None))
        self.Medicine_name_2.setText(QCoreApplication.translate("Form", u"Medicine Name ", None))
        self.Medicine_usage_2.setText(QCoreApplication.translate("Form", u" Medicine Usage", None))
        self.Price_2.setText(QCoreApplication.translate("Form", u"Price ", None))
        self.Count_2.setText(QCoreApplication.translate("Form", u"count", None))
        self.Medicine_name_4.setText(QCoreApplication.translate("Form", u"Medicine Name ", None))
        self.Medicine_usage_4.setText(QCoreApplication.translate("Form", u" Medicine Usage", None))
        self.Price_4.setText(QCoreApplication.translate("Form", u"Price ", None))
        self.lineEdit_11.setText(QCoreApplication.translate("Form", u"count", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Report", None))
        self.Total_Price_Label.setText(QCoreApplication.translate("Form", u"Total Price", None))
    # retranslateUi

