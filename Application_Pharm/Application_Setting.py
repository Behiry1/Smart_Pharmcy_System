import sys
import re
import json

from PySide6.QtCore import QPropertyAnimation, QFile, QEasingCurve
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

# Import QTimer
from PySide6.QtCore import QTimer

import time


from Final_Main_ui import Ui_MainWindow
from Datbase_Setting import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.comboBox.hide()
        self.HideCenterMenuPages()
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
        self.ui.pushButton_3.clicked.connect(self.GoReg)
        self.ui.pushButton_2.clicked.connect(self.GoLog)
        self.ui.pushButton_4.clicked.connect(self.Login)
        self.ui.pushButton.clicked.connect(self.Register)
        self.ui.radioButton_Dr.clicked.connect(self.ShowDepartement)
        self.ui.radioButton_pharm.clicked.connect(self.HideDepartement)
        self.ui.menuBtn.clicked.connect(self.ShowCenterMenuPages)
        self.ui.closeCenterMenuBtn.clicked.connect(self.HideCenterMenuPages)


    def ShowCenterMenuPages(self):
        self.ui.centerMenuSubContainer.show()
    def HideCenterMenuPages(self):
        self.ui.centerMenuSubContainer.hide()

    def GoReg(self):
        clear_errors(self.ui)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.RegisterPage)

    def GoLog(self):
        clear_errors(self.ui)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.LoginPage)
    def GoMain(self):
        clear_errors(self.ui)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)
    def Register(self):
        email = self.ui.lineEdit_5.text().strip()
        password = self.ui.lineEdit_2.text().strip()
        confirm_password = self.ui.lineEdit_3.text().strip()
        first_name = self.ui.lineEdit.text().strip()
        last_name = self.ui.lineEdit_4.text().strip()
        phone_number = self.ui.lineEdit_6.text().strip()
        department = self.ui.comboBox.currentText()

        if not email or not password or not first_name or not last_name or not phone_number:
            show_registration_error(self.ui, "Please fill in all fields.")
            return

        if not self.validate_password(password):
            show_registration_error(self.ui, "Password must be at least 8 characters.")
            return

        if not self.validate_phoneNumber(phone_number):
            show_registration_error(self.ui, "Please enter a valid number.")
            return

        if not self.validate_email(email):
            show_registration_error(self.ui, "Invalid email address.")
            return

        if not self.validate_passwords(password,confirm_password):
            show_registration_error(self.ui, "Passwords do not match")
            return

        if self.ui.radioButton_Dr.isChecked():
           fl =  doctor_register(self.ui, email, password, first_name, last_name, phone_number, department)
           if(fl == True):

               QTimer.singleShot(500, self.GoLog)

        elif self.ui.radioButton_pharm.isChecked():
           fl =  pharmacist_register(self.ui, email, password, first_name, last_name, phone_number)

           if(fl == True):

               QTimer.singleShot(500, self.GoLog)

        elif not self.ui.radioButton_Dr.isChecked() and not self.ui.radioButton_pharm.isChecked():

            show_registration_error(self.ui,"Please select your identity.")


    def Login(self):
        email = self.ui.lineEdit_7.text().strip()
        password = self.ui.lineEdit_8.text().strip()

        if not email or not password:
            show_login_error(self.ui, "Please enter email and password.")
            return

        fl = login_user(self.ui, email, password)

        if(fl == True):


            QTimer.singleShot(500, self.GoMain)






    def ShowDepartement(self):
        self.ui.comboBox.show()

    def HideDepartement(self):
        self.ui.comboBox.hide()

    def validate_email(self,email):
        email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
        return re.match(email_regex, email) is not None

    def validate_password(self,password):
       return len(password) >= 8

    def validate_passwords(self,password, confirm_password):
        if password != confirm_password:
            return False
        else:
            return True

    def validate_phoneNumber(self, phoneNumber):
        if len(phoneNumber) != 11:
            return False
        if not phoneNumber.isdigit():
            return False
        return True

def StartApplication():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())


