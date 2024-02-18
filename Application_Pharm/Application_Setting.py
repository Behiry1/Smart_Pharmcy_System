import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Login_SignUp_Ui import Ui_MainWindow
from Datbase_Setting import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.comboBox.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
        self.ui.pushButton_3.clicked.connect(self.GoReg)
        self.ui.pushButton_2.clicked.connect(self.GoLog)
        self.ui.pushButton_4.clicked.connect(self.Login)
        self.ui.pushButton.clicked.connect(self.Register)
        self.ui.radioButton_Dr.clicked.connect(self.ShowDepartement)
        self.ui.radioButton_pharm.clicked.connect(self.HideDepartement)

    def GoReg(self):
        clear_errors(self.ui)
        self.ui.stackedWidget.setCurrentWidget(self.ui.RegisterPage)

    def GoLog(self):
        clear_errors(self.ui)
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    def Register(self):
        email = self.ui.lineEdit_5.text().strip()
        password = self.ui.lineEdit_2.text().strip()
        first_name = self.ui.lineEdit.text().strip()
        last_name = self.ui.lineEdit_4.text().strip()
        phone_number = self.ui.lineEdit_6.text().strip()
        department = self.ui.comboBox.currentText()

        if not email or not password or not first_name or not last_name or not phone_number:
            show_registration_error(self.ui, "Please fill in all fields.")
            return

        if self.ui.radioButton_Dr.isChecked():
            doctor_register(self.ui, email, password, first_name, last_name, phone_number, department)
        elif self.ui.radioButton_pharm.isChecked():
            pharmacist_register(self.ui, email, password, first_name, last_name, phone_number)

    def Login(self):
        email = self.ui.lineEdit_7.text().strip()
        password = self.ui.lineEdit_8.text().strip()

        if not email or not password:
            show_login_error(self.ui, "Please enter email and password.")
            return

        login_user(self.ui, email, password)

    def ShowDepartement(self):
        self.ui.comboBox.show()

    def HideDepartement(self):
        self.ui.comboBox.hide()

def StartApplication():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())

