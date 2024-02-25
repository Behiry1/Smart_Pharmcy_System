import sys


from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QGridLayout, QCheckBox, \
    QLabel, QWidget
from SignUp_Login import *
class Dr_MainWindow(MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)



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
        self.ui.homeBtn.clicked.connect(self.HomePage)
        self.FreezeColor("homeBtn")


             #orderBtn
        self.ui.orderBtn.clicked.connect(self.OrderPage)


             #reportsBtn
        self.ui.reportsBtn.clicked.connect(self.ReportsPage)

             #search_btn
        self.ui.lineEdit_9.textEdited.connect(self.Search)
        #self.ui.pushButton_23.clicked.connect(self.SearchBtnClicked)
        self.SearchBtn_Flag = False

        self.scroll_area = self.ui.scrollArea
        self.scroll_content = QWidget()  # Create a QWidget to hold the frames
        self.scroll_area.setWidgetResizable(True)

        self.scroll_layout = QGridLayout(self.scroll_content)  # Create a QGridLayout for the scroll content
        #self.scroll_layout.setAlignment(Qt.AlignTop)  # Align the layout to the top



    def Search(self):
        text = self.ui.lineEdit_9.text()
        if len(text) >= 6:
            # Perform the search in the database
            search_results = search_medicine_data(text)
            if search_results:
                # Clear existing frames before adding new ones
                self.ClearFrames()

                # Add frames for each search result
                self.AddFrames(search_results)
            else:
                print("Medicine not found")

        else:
            print("Please enter at least 6 characters for search")

    def AddFrames(self, search_results):
        self.ui.scrollArea.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_content.setLayout(self.scroll_layout)

        frame_count = len(search_results)
        rows = (frame_count + 2) // 3  # Calculate number of rows needed for 3 columns

        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Set alignment to top-left
        self.scroll_layout.addLayout(grid_layout)

        for i, result in enumerate(search_results):
            english_name = result['English_Name']
            medicine_price = result['Medicine_Price']
            active_substance = result['Active_Substance']
            frame = self.create_frame(english_name, medicine_price, active_substance)
            row = i // 3
            col = i % 3
            grid_layout.addWidget(frame, row, col)

        self.ui.scrollArea.setWidget(self.scroll_content)

    def create_frame(self, english_name, medicine_price, active_substance):
        frame = QFrame()
        frame.setFixedSize(500, 150)  # Set fixed size for the frame

        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        layout = QGridLayout()
        frame.setLayout(layout)

        layout.addWidget(QLabel("English Name:"), 0, 0)
        layout.addWidget(QLabel(english_name), 0, 1)
        layout.addWidget(QLabel("Medicine Price:"), 1, 0)
        layout.addWidget(QLabel(str(medicine_price)), 1, 1)
        layout.addWidget(QLabel("Active Substance:"), 2, 0)
        layout.addWidget(QLabel(active_substance), 2, 1)
        layout.addWidget(QCheckBox("Select"), 3, 0)
        layout.addWidget(QPushButton("Add to Favorite"), 3, 1)

        return frame

    def ClearFrames(self):
        # Remove all existing frames from the scroll area
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def CenterMenuPages(self):
        if self.menuBtn_Flag:
            self.ui.centerMenuContatiner.show()
            self.FreezeColor("menuBtn")
        else:
            self.ui.centerMenuContatiner.hide()
            self.ClearBackGround_Color("menuBtn")
        self.menuBtn_Flag = not self.menuBtn_Flag


    def Notification(self):
        if self.notificationBtn_Flag:
            self.ui.popupNotificationSubContainer.show()
            self.FreezeColor("notificationBtn")
        else:
            self.ui.popupNotificationSubContainer.hide()
            self.ClearBackGround_Color("notificationBtn")
        self.notificationBtn_Flag = not self.notificationBtn_Flag
    def HomePage(self):
        self.ui.mainPages.setCurrentWidget(self.ui.homePage)
        self.FreezeColor("homeBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("reportsBtn")


    def OrderPage(self):
        self.ui.mainPages.setCurrentWidget(self.ui.orderPage)
        self.FreezeColor("orderBtn")
        self.ClearBackGround_Color("reportsBtn")
        self.ClearBackGround_Color("homeBtn")

    def ReportsPage(self):
        self.ui.mainPages.setCurrentWidget(self.ui.reportsPage)
        self.FreezeColor("reportsBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("homeBtn")

    def FreezeColor(self, button):
        self.buttons = [
            self.ui.menuBtn,
            self.ui.homeBtn,
            self.ui.orderBtn,
            self.ui.reportsBtn,
            self.ui.helpBtn,
            self.ui.infoBtn,
            self.ui.settingsBtn,
            self.ui.notificationBtn,
        ]

        for btn in self.buttons:
            if btn.objectName() == button:
                btn.setStyleSheet("background-color: rgb(18, 163, 176)")

    def ClearBackGround_Color(self,button):
        self.buttons = [
            self.ui.menuBtn,
            self.ui.homeBtn,
            self.ui.orderBtn,
            self.ui.reportsBtn,
            self.ui.helpBtn,
            self.ui.infoBtn,
            self.ui.settingsBtn,
            self.ui.notificationBtn,
        ]
        for btn in self.buttons:
            if btn.objectName() == button:
                btn.setStyleSheet("background-color: transparent")
                btn.setStyleSheet("QPushButton:hover {background-color:rgb(28, 171, 213)}")




def StartApplication():
    app = QApplication(sys.argv)
    mainWindow = Dr_MainWindow()
    sys.exit(app.exec())


