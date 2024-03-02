import re
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout

import Dr_MainWindow
from Datbase_Setting import clear_errors
from Final_Main_ui import Ui_MainWindow
from Datbase_Setting import *
from Dr_MainWindow import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        # show Ui pages
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()



        # Sihnup_btns,funs
        self.HideDepartement()
        self.ui.pushButton_2.clicked.connect(self.GoLog)
        self.ui.radioButton_Dr.clicked.connect(self.ShowDepartement)
        self.ui.radioButton_pharm.clicked.connect(self.HideDepartement)
        self.ui.pushButton.clicked.connect(self.Register)

        # Login_btns,funs
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)
        self.ui.pushButton_3.clicked.connect(self.GoReg)
        self.ui.pushButton_4.clicked.connect(self.Login)
        self.login_Fl = False

        #dr_MainPage_btns,funs
             #Menu_btn
        self.ui.centerMenuContatiner.hide()
        self.ui.menuBtn.clicked.connect(self.CenterMenuPages)
        self.menuBtn_Flag = True

             #notification_btn
        self.ui.popupNotificationSubContainer.hide()
        self.ui.notificationBtn.clicked.connect(self.Notification)
        self.notificationBtn_Flag = True



             #home_Btn
        self.ui.rightMenuSubContainer.show()
        self.ui.homeBtn.clicked.connect(self.HomePage)
        self.FreezeColor("homeBtn")


             #orderBtn
        self.ui.orderBtn.clicked.connect(self.OrderPage)


             #reportsBtn
        self.ui.reportsBtn.clicked.connect(self.ReportsPage)

             #search_btn
        self.ui.lineEdit_9.textEdited.connect(self.Search)







        self.ClearFrames()
        self.clear_scroll_area_2()
        self.favorite_state = {}
        self.favorite_medicines = []
        self.Selected_Medicine = []
        #self.add_widgets_to_scrollarea3()
        self.ui.pushButton_13.clicked.connect(self.Create_Prescription)
        self.ui.Print_button.clicked.connect(self.Print)




    def GoReg(self):
            clear_errors(self.ui)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.RegisterPage)

    def GoLog(self):
            clear_errors(self.ui)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.LoginPage)

    def GoMain(self):
            clear_errors(self.ui)
            self.ui.stackedWidget.setCurrentWidget(self.ui.Main_page)



    def ShowDepartement(self):
            self.ui.comboBox.show()

    def HideDepartement(self):
            self.ui.comboBox.hide()

    def validate_email(self, email):
            email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
            return re.match(email_regex, email) is not None

    def validate_password(self, password):
            return len(password) >= 8

    def validate_passwords(self, password, confirm_password):
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



    def SetFlagTrue(self):
        return self.login_Fl