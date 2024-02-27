import sys
from PySide6.QtCore import Qt, QSize, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QGridLayout, QCheckBox, \
    QLabel, QWidget
from SignUp_Login import *
from Datbase_Setting import *
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
        self.scroll_area = self.ui.scrollArea
        self.scroll_content = QWidget()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_layout = QGridLayout(self.scroll_content)
        self.StartUpMedicine()
        self.ClearFrames()
        self.clear_scroll_area_2()
        self.favorite_state = {}
        self.favorite_medicines = []


    def StartUpMedicine(self):
        all_results = SearchStartUpMedicine()

        if all_results:
            self.AddFrames(all_results)
        else:
            print("No medicines found.")

    def Search(self):
        text = self.ui.lineEdit_9.text()
        if len(text) >= 6:
            search_results = search_medicine_data(text)
            if search_results:
                self.ClearFrames()
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
        rows = (frame_count + 2) // 3

        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.scroll_layout.addLayout(grid_layout)

        scroll_width = self.ui.scrollArea.viewport().size().width()
        card_width = scroll_width // 3

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

        layout.addWidget(QLabel("English Name:"), 1, 0)
        layout.addWidget(QLabel(english_name), 1, 1)
        layout.addWidget(QLabel("Medicine Price:"), 3, 0)
        layout.addWidget(QLabel(str(medicine_price)), 3, 1)
        layout.addWidget(QLabel("Active Substance:"), 2, 0)
        layout.addWidget(QLabel(active_substance), 2, 1)
        layout.addWidget(QCheckBox("Select"), 0, 0)
        button = QPushButton("")
        button.setStyleSheet("max-width: 30px")
        layout.addWidget(button, 0, 3)

        button.clicked.connect(lambda: self.toggle_favorite(english_name, active_substance, button))

        return frame

    def toggle_favorite(self, english_name, active_substance, button):
        if (english_name, active_substance) not in self.favorite_state:
            # Item is not favorited yet
            self.favorite_state[(english_name, active_substance)] = True
            self.favorite_action(english_name, active_substance)
            # Change button style to indicate favorited state
            self.favorite_medicines.append((english_name, active_substance))
            button.setStyleSheet(
                "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
        else:
            # Item is already favorited
            if self.favorite_state[(english_name, active_substance)]:
                # Perform action when unfavoriting
                self.unfavorite_action(english_name, active_substance)
                if (english_name, active_substance) in self.favorite_medicines:
                    self.favorite_medicines.remove((english_name, active_substance))
                # Change button style to indicate unfavorited state
                button.setStyleSheet("max-width: 30px;min-height:20px")  # Reset style to default
            else:
                # Perform action when favoriting again
                self.favorite_action(english_name, active_substance)
                # Change button style to indicate favorited state
                button.setStyleSheet(
                    "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
                self.favorite_medicines.append((english_name, active_substance))

            # Toggle the favorite state
            self.favorite_state[(english_name, active_substance)] = not self.favorite_state[
                (english_name, active_substance)]
            print(self.favorite_state)

        # Retrieve medicine IDs for all favorite medicines
        medicine_ids = []
        for med_name, med_substance in self.favorite_medicines:
            med_id = get_medicine_id(med_name, med_substance)
            if med_id:
                medicine_ids.append(med_id)

        # Update the UI
        self.display_favorite_medicines()

        # Get doctor ID from email and update favorite medicines in the database
        self.drid = get_dr_id_from_email(self.ui.lineEdit_7.text().strip())
        add_to_favorite(self.drid, medicine_ids)
    def favorite_action(self, english_name, active_substance):
        # Action to perform when favoriting
        print(f"{english_name} with active substance {active_substance} favorited")
        print(self.favorite_medicines)

    def unfavorite_action(self, english_name, active_substance):
        # Action to perform when unfavoriting
        print(f"{english_name} with active substance {active_substance} unfavorited")

    def create_favorite_frame(self, english_name, active_substance):
        frame = QFrame()
        frame.setObjectName("Cared_13")
        frame.setGeometry(QRect(9, 201, 187, 100))
        frame.setMinimumSize(QSize(50, 85))
        frame.setMaximumSize(QSize(16777215, 100))
        frame.setAutoFillBackground(False)
        frame.setStyleSheet("")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        gridLayout = QGridLayout(frame)
        gridLayout.setObjectName("gridLayout_15")

        checkBox = QCheckBox("Select")
        gridLayout.addWidget(checkBox, 0, 0, 1, 1)

        label_name = QLabel(english_name)
        gridLayout.addWidget(label_name, 1, 0, 1, 1)

        label_substance = QLabel(active_substance)
        gridLayout.addWidget(label_substance, 3, 0, 1, 1)

        pushButton = QPushButton()
        pushButton.setMinimumSize(QSize(20, 20))
        pushButton.setMaximumSize(QSize(15, 15))
        pushButton.setText("")
        pushButton.setIconSize(QSize(16, 16))
        gridLayout.addWidget(pushButton, 0, 2, 1, 1)

        return frame

    def get_frame_style(self):
        return """
            border: 2px solid black;
            border-radius: 5px;
            background-color: #f0f0f0;
            padding: 5px;
        """

    def display_favorite_medicines(self):
        self.clear_scroll_area_2()

        layout = QVBoxLayout()  # Use QVBoxLayout instead of QGridLayout
        for name, substance in self.favorite_medicines:
            frame = self.create_favorite_frame(name, substance)
            layout.addWidget(frame)

        # Add a stretch to the layout to push the frames to the top
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        self.ui.scrollArea_2.setWidget(widget)

    def clear_scroll_area_2(self):
        if self.ui.scrollArea_2.layout() is not None:
            for i in reversed(range(self.ui.scrollArea_2.layout().count())):
                widget = self.ui.scrollArea_2.layout().itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

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

    def update_frame_width(self):
        if self.scroll_layout is None:
            return  # If scroll_layout is not initialized, return

        scroll_width = self.ui.scrollArea.viewport().size().width()
        columns = 3
        card_width = scroll_width // columns

        # Update the width of frames inside the scroll area
        for i in range(self.scroll_layout.count()):
            frame = self.scroll_layout.itemAt(i).widget()
            if frame is not None:
                frame.setFixedWidth(card_width - 10)




def StartApplication():
    app = QApplication(sys.argv)
    mainWindow = Dr_MainWindow()
    sys.exit(app.exec())


