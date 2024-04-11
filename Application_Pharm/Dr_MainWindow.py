import Dr_MainWindow_Database
from Dr_MainWindow_Database import search_medicine_data,retrieve_medicine_info
from PySide6.QtWidgets import QMainWindow, QSpacerItem
from Final_Main_ui import Ui_Dr_MainWindow  # Update the import statement
from Dr_MainWindow_Functions import Favorite_Functions,MainPages_Functions,Prescription_Functions
from Dr_MainWindow_Orientation import *
from PySide6.QtCore import Qt

class Dr_MainWindow(QMainWindow, Ui_Dr_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.favorite_state = {}
        self.favorite_medicines = []
        self.Selected_Medicine = []
        self.Startup_DrWindow()


    def Startup_DrWindow(self):
        self.setupUi(self)  # Setup the user interface
        Favorite_Orientation.clear_scroll_area_2(self)  # Clear scroll area if needed
        Prescription_Orientation.Clear_Prescription_Page(self)
        self.lineEdit_9.textEdited.connect(self.Search)
        self.pushButton_13.clicked.connect(lambda: Prescription_Orientation.Create_Prescription(self))
        self.Print_button.clicked.connect(lambda: Prescription_Functions.Print(self))
        self.menuBtn.clicked.connect(self.CenterMenuPages)
        self.notificationBtn.clicked.connect(self.Notification)
        self.homeBtn.clicked.connect(self.HomePage)
        self.orderBtn.clicked.connect(self.OrderPage)
        self.reportsBtn.clicked.connect(self.ReportsPage)

        # Initialize UI elements and flags
        self.centerMenuContatiner.hide()
        self.popupNotificationSubContainer.hide()
        self.menuBtn_Flag = True
        self.notificationBtn_Flag = True
        self.mainPages.setCurrentWidget(self.homePage)
        self.rightMenuSubContainer.show()
        self.FreezeColor("homeBtn")

        # Load data or perform any other necessary setup steps
        MainPages_Functions.StartUpMedicine(self)
        Favorite_Functions.load_favorite_data(self, self.favorite_medicines, self.favorite_state)
        History_Orientation.Clear_History_Page(self)
        History_Orientation.Load_History_Prescription(self)
        self.lineEdit_11.textChanged.connect(self.Search_Prescription)


        # Show the main window
        self.show()



    def Search_Prescription(self):
        text = self.lineEdit_11.text().strip().lower()
        search_results = Dr_MainWindow_Database.search_prescription_by_id_or_name(text)
        if search_results:
            History_Orientation.Clear_History_Page(self)
            self.Add_SearchResults(search_results)
        else:
            History_Orientation.Clear_History_Page(self)
            print("Patient Not Found!")

    def Add_SearchResults(self, prescription_details):
        # Create widget to hold the content
        History_Orientation.Clear_History_Page(self)
        content_widget = QWidget(self.scrollArea_4)
        content_layout = QVBoxLayout(content_widget)

        # Clear existing layout
        while content_layout.count():
            child = content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Add widgets created by create_history_widgets to the content layout
        for prescription in prescription_details:
            prescription_widget = History_Orientation.create_history_widgets(self,prescription[0], prescription[1], prescription[2])
            content_layout.addWidget(prescription_widget)

        # Set the content widget for the scroll area
        self.scrollArea_4.setWidget(content_widget)

    def Search(self):
        text = self.lineEdit_9.text()
        if len(text) >= 6:
            search_results = search_medicine_data(text)
            if search_results:
                MainPages_Orientation.Clear_Medicine_Frames(self)
                MainPages_Orientation.AddFrames(self,search_results)
            else:

                print("Medicine not found")
        elif len(text) == 0:
            MainPages_Functions.StartUpMedicine(self)
        else:

            print("Please enter at least 6 characters for search")
    def CenterMenuPages(self):
        if self.menuBtn_Flag:
            self.centerMenuContatiner.show()
            self.FreezeColor("menuBtn")
        else:
            self.centerMenuContatiner.hide()
            self.ClearBackGround_Color("menuBtn")
        self.menuBtn_Flag = not self.menuBtn_Flag
    def Notification(self):
        if self.notificationBtn_Flag:
            self.popupNotificationSubContainer.show()
            self.FreezeColor("notificationBtn")
        else:
            self.popupNotificationSubContainer.hide()
            self.ClearBackGround_Color("notificationBtn")
        self.notificationBtn_Flag = not self.notificationBtn_Flag
    def HomePage(self):
        self.mainPages.setCurrentWidget(self.homePage)
        self.rightMenuSubContainer.show()
        self.FreezeColor("homeBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("reportsBtn")
    def OrderPage(self):
        self.mainPages.setCurrentWidget(self.orderPage)
        self.rightMenuSubContainer.hide()
        self.FreezeColor("orderBtn")
        self.ClearBackGround_Color("reportsBtn")
        self.ClearBackGround_Color("homeBtn")
    def ReportsPage(self):
        self.mainPages.setCurrentWidget(self.reportsPage)
        self.rightMenuSubContainer.hide()
        self.FreezeColor("reportsBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("homeBtn")
    def FreezeColor(self, button):
        self.buttons = [
            self.menuBtn,
            self.homeBtn,
            self.orderBtn,
            self.reportsBtn,
            self.helpBtn,
            self.infoBtn,
            self.settingsBtn,
            self.notificationBtn,
        ]

        for btn in self.buttons:
            if btn.objectName() == button:
                btn.setStyleSheet("background-color: rgb(18, 163, 176)")
    def ClearBackGround_Color(self, button):
        self.buttons = [
            self.menuBtn,
            self.homeBtn,
            self.orderBtn,
            self.reportsBtn,
            self.helpBtn,
            self.infoBtn,
            self.settingsBtn,
            self.notificationBtn,
        ]
        for btn in self.buttons:
            if btn.objectName() == button:
                btn.setStyleSheet("background-color: transparent")
                btn.setStyleSheet("QPushButton:hover {background-color:rgb(28, 171, 213)}")






