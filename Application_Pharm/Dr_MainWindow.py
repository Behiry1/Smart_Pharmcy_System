import sys
import mysql.connector
from PySide6.QtCore import Qt, QSize, QRect, QUrl
from PySide6.QtGui import QIcon, QFont, QPainter, QPixmap, QPageSize, QDesktopServices, QPdfWriter, QFontMetrics
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QGridLayout, QCheckBox, \
    QLabel, QWidget, QLineEdit, QHBoxLayout, QFileDialog
from SignUp_Login import *
from Datbase_Setting import *


class Dr_MainWindow(MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)


    def load_favorite_data(self):
        print("Welcome")
        email = self.ui.lineEdit_7.text().strip()
        self.drid = get_dr_id_from_email(email)
        favorite_medicines = load_favorite_medicines(self.drid)

        if favorite_medicines:
            self.favorite_medicines = favorite_medicines

            for m in favorite_medicines:
                english_name = m[0]  # Access the first element of the tuple
                active_substance = m[1]  # Access the second element of the tuple
                # Update favorite state for each medicine
                self.favorite_state[(english_name, active_substance)] = True

            self.display_favorite_medicines()
        else:
            print("No favorite medicines found for this doctor ID.")

    def StartUpMedicine(self):
        all_results = SearchStartUpMedicine()

        email = self.ui.lineEdit_7.text().strip()
        self.drid = get_dr_id_from_email(email)

        if all_results:
            # Fetch favorite medicines
            favorite_medicines = load_favorite_medicines(self.drid)
              # Dictionary to store favorite states for each medicine
            for result in all_results:
                english_name = result['English_Name']
                active_substance = result['Active_Substance']
                self.favorite_state[(english_name, active_substance)] = False  # Initialize all to unfavorited

            # Check favorite medicines and set their button states
            if favorite_medicines:
                for result in all_results:
                    english_name = result['English_Name']
                    active_substance = result['Active_Substance']
                    if (english_name, active_substance) in favorite_medicines:
                        self.favorite_state[(english_name, active_substance)] = True

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
        elif len(text) == 0:
            self.StartUpMedicine()
        else:
            print("Please enter at least 6 characters for search")

    def create_widget(self, medicine_info):
        self.clear_scroll_area3()

        widget = QFrame()
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setMinimumSize(561, 35)
        frame.setMaximumSize(16777215, 35)

        inner_layout = QHBoxLayout()
        inner_layout.setSpacing(0)
        inner_layout.setContentsMargins(0, 0, 0, 0)

        # Medicine Name
        medicine_name = QLabel(medicine_info.get('English_Name', 'N/A'))
        medicine_name.setMinimumSize(210, 35)
        medicine_name.setFont(QFont())
        inner_layout.addWidget(medicine_name)

        # Medicine Usage
        usage = QLabel(medicine_info.get('Medicine_Usage', 'N/A'))
        usage.setMinimumSize(200, 35)
        usage.setFont(QFont())
        inner_layout.addWidget(usage)

        # Price
        price = QLabel(str(medicine_info.get('Medicine_Price', 'N/A')))
        price.setMinimumSize(50, 35)
        price.setMaximumSize(150, 35)
        price.setFont(QFont())
        inner_layout.addWidget(price)

        # Count QLineEdit
        count_edit = QLineEdit("count")
        count_edit.setMinimumSize(50, 35)
        count_edit.setMaximumSize(120, 35)
        count_edit.setFont(QFont())
        inner_layout.addWidget(count_edit)

        # Delete Button
        delete_button = QPushButton()
        delete_button.setMaximumSize(35, 35)
        delete_button.setIcon(QIcon(":/Icon_web/Image_for_main/icons_from_Web/trash-2.svg"))
        delete_button.setStyleSheet("border: 1px solid #064666; margin: 2px;")
        inner_layout.addWidget(delete_button)

        frame.setLayout(inner_layout)
        layout.addWidget(frame)

        widget.setLayout(layout)

        return widget

    def add_widgets_to_scrollarea3(self):

        scroll_layout1 = self.ui.scrollArea_3.layout()

        if scroll_layout1 is None:
            scroll_layout1 = QVBoxLayout()
            self.ui.scrollArea_3.setLayout(scroll_layout1)

        added_widgets = {}

        for medicine_name in self.Selected_Medicine:
            # Check if the widget for the current medicine name already exists
            if medicine_name in added_widgets:
                continue

            # Retrieve medicine information from the database
            medicine_info = get_medicine_info(medicine_name)

            if medicine_info:
                # Create a widget using the retrieved information
                widget = self.create_widget(medicine_info)
                # Add the widget to the scroll area
                widget.setFixedSize(16777215, 35)  # Set fixed size for the widget
                scroll_layout1.addWidget(widget)  # Add widget to the layout
                # Store the widget in the dictionary
                added_widgets[medicine_name] = widget
        print(added_widgets)

    def clear_scroll_area3(self):
        # Get the scroll area's content widget
        scroll_content1 = self.ui.scrollArea_3.widget()

        # Clear existing layout and widgets
        if scroll_content1 is not None:
            # Remove the content widget from the scroll area
            self.ui.scrollArea_3.takeWidget()

            # Delete the content widget
            scroll_content1.deleteLater()

    def Create_Prescription(self):
        self.OrderPage()

        # Clear the scroll area before adding new widgets
        self.clear_scroll_area3()

        # Add widgets to the scroll area
        self.add_widgets_to_scrollarea3()

    def Print(self):
        # Create a PDF writer object
        pdf_filename = "output.pdf"
        pdf_writer = QPdfWriter(pdf_filename)

        # Configure the PDF writer
        pdf_writer.setPageSize(QPageSize(QPageSize.A5))
        pdf_writer.setResolution(300)  # Set resolution

        # Create a painter object to draw on the PDF
        painter = QPainter(pdf_writer)

        # Calculate available space for content
        available_width = pdf_writer.width()
        available_height = pdf_writer.height()

        # Calculate the size of the custom frame in millimeters
        frame_width_mm = 140
        frame_height_mm = 500

        # Calculate the size of the frame in pixels
        dpi_x = pdf_writer.logicalDpiX()
        dpi_y = pdf_writer.logicalDpiY()
        frame_width_pixels = dpi_x * frame_width_mm / 25.4
        frame_height_pixels = dpi_y * frame_height_mm / 25.4

        # Resize the widget to match the dimensions of the custom frame
        self.ui.orderPage.resize(frame_width_pixels, frame_height_pixels)

        # Set font size using stylesheet for the OrderPage widget
        font_stylesheet = """
            font-size: 20pt;
            color: black;
            border: 2px solid black;
            background-color: #f0f0f0; /* Background color */
            border-radius: 10px; /* Rounded corners */
            max-height: 1080px; /* Set a reliable maximum height */
        }
          
        """

        self.ui.orderPage.setStyleSheet(font_stylesheet)


        # Create a pixmap to render the OrderPage widget onto it
        pixmap = QPixmap(self.ui.orderPage.size())
        pixmap.fill(Qt.white)  # Fill pixmap with white background
        self.ui.orderPage.render(pixmap)

        # Draw the pixmap onto the PDF
        painter.drawPixmap(0, 0, pixmap)

        # Close the painter
        painter.end()

        # Open the PDF file using a PDF viewer
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_filename))
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

        # Create Select checkbox
        select_checkbox = QCheckBox("Select")
        layout.addWidget(select_checkbox, 0, 0)

        # Create heart button
        button = QPushButton("")
        button.setStyleSheet("max-width: 30px")
        layout.addWidget(button, 0, 3)

        # Set initial state of heart button based on whether the medicine is in favorite list
        if (english_name, active_substance) in self.favorite_state:
            if self.favorite_state[(english_name, active_substance)]:
                button.setStyleSheet(
                    "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")

        button.clicked.connect(lambda: self.toggle_favorite(english_name, active_substance, button))

        if(english_name) in self.Selected_Medicine:
            select_checkbox.setChecked(True)

        # Connect the clicked signal of the checkbox to the checkbox_clicked slot function
        select_checkbox.clicked.connect(
            lambda checked: self.checkbox_clicked(checked, english_name, active_substance))


        return frame

    def checkbox_clicked(self, checked, english_name, active_substance):
        if checked:
            # Checkbox is checked
            print(f"{english_name} with active substance {active_substance} is selected.")
            # Add the English name of the selected medicine to the Selected_Medicine array
            self.Selected_Medicine.append(english_name)
            # Perform certain function here (if needed)
        else:
            # Checkbox is unchecked
            print(f"{english_name} with active substance {active_substance} is deselected.")
            # Remove the English name of the deselected medicine from the Selected_Medicine array (if it exists)
            if english_name in self.Selected_Medicine:
                self.Selected_Medicine.remove(english_name)
            # Perform certain function here (if needed)
        print(self.Selected_Medicine)
        self.display_favorite_medicines()

    def toggle_favorite(self, english_name, active_substance, button):
        if (english_name, active_substance) not in self.favorite_state:
            # Item is not favorited yet
            self.favorite_state[(english_name, active_substance)] = True
            self.favorite_medicines.append((english_name, active_substance))
            button.setStyleSheet(
                "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
        else:
            # Toggle the favorite state
            self.favorite_state[(english_name, active_substance)] = not self.favorite_state[
                (english_name, active_substance)]

            if self.favorite_state[(english_name, active_substance)]:
                # Perform action when favoriting again
                self.favorite_medicines.append((english_name, active_substance))
                button.setStyleSheet(
                    "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
            else:
                # Perform action when unfavoriting
                if (english_name, active_substance) in self.favorite_medicines:
                    self.favorite_medicines.remove((english_name, active_substance))
                button.setStyleSheet("max-width: 30px;min-height:20px")  # Reset style to default

        # Retrieve medicine IDs for all favorite medicines
        medicine_ids = [get_medicine_id(name, substance) for name, substance in self.favorite_medicines]

        # Update the UI
        self.display_favorite_medicines()

        # Update favorite medicines in the database
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

        # Connect lambda function to remove the medicine from favorites
        pushButton.clicked.connect(lambda: self.remove_from_favorites(english_name, active_substance, frame))

        if(english_name) in self.Selected_Medicine:
            checkBox.setChecked(True)

        checkBox.clicked.connect(
            lambda checked: self.checkbox_clicked_favorite(checked, english_name, active_substance))

        return frame

    def checkbox_clicked_favorite(self,checked,english_name,active_substance):
        if checked:
            # Checkbox is checked
            print(f"{english_name} with active substance {active_substance} is selected.")
            # Add the English name of the selected medicine to the Selected_Medicine array
            self.Selected_Medicine.append(english_name)
            # Perform certain function here (if needed)
        else:
            # Checkbox is unchecked
            print(f"{english_name} with active substance {active_substance} is deselected.")
            # Remove the English name of the deselected medicine from the Selected_Medicine array (if it exists)
            if english_name in self.Selected_Medicine:
                self.Selected_Medicine.remove(english_name)
            # Perform certain function here (if needed)
        print(self.Selected_Medicine)
        self.Search()

    def remove_from_favorites(self, english_name, active_substance, frame):
        # Remove medicine from the favorite list
        self.favorite_medicines.remove((english_name, active_substance))
        self.favorite_state[(english_name, active_substance)] = False

        #self.update_main_frames_favorite_state()
        #self.toggle_favorite(english_name,active_substance,None)
        # Update UI to remove the frame of the removed medicine
        frame.deleteLater()

        # Update favorite medicines in the database
        self.drid = get_dr_id_from_email(self.ui.lineEdit_7.text().strip())
        self.mid = get_medicine_id(english_name, active_substance)
        delete_from_favorite(self.drid,self.mid)
        self.Search()


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
        self.scroll_content = QWidget()
        # self.scroll_area.setWidgetResizable(True)
        self.scroll_layout = QGridLayout(self.scroll_content)
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
        self.ui.rightMenuSubContainer.show()
        self.FreezeColor("homeBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("reportsBtn")


    def OrderPage(self):
        self.ui.mainPages.setCurrentWidget(self.ui.orderPage)
        self.ui.rightMenuSubContainer.hide()
        self.FreezeColor("orderBtn")
        self.ClearBackGround_Color("reportsBtn")
        self.ClearBackGround_Color("homeBtn")

    def ReportsPage(self):
        self.ui.mainPages.setCurrentWidget(self.ui.reportsPage)
        self.ui.rightMenuSubContainer.hide()
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

        if not self.validate_passwords(password, confirm_password):
            show_registration_error(self.ui, "Passwords do not match")
            return

        if self.ui.radioButton_Dr.isChecked():
            fl = doctor_register(self.ui, email, password, first_name, last_name, phone_number, department)
            if (fl == True):
                QTimer.singleShot(500, self.GoLog)

        elif self.ui.radioButton_pharm.isChecked():
            fl = pharmacist_register(self.ui, email, password, first_name, last_name, phone_number)

            if (fl == True):
                QTimer.singleShot(500, self.GoLog)

        elif not self.ui.radioButton_Dr.isChecked() and not self.ui.radioButton_pharm.isChecked():

            show_registration_error(self.ui, "Please select your identity.")

    def Login(self):
        email = self.ui.lineEdit_7.text().strip()
        password = self.ui.lineEdit_8.text().strip()

        if not email or not password:
            show_login_error(self.ui, "Please enter email and password.")
            return

        fl = login_user(self.ui, email, password)

        if (fl == True):
            QTimer.singleShot(500, self.GoMain)
            self.load_favorite_data()
            self.StartUpMedicine()




def StartApplication():
    app = QApplication(sys.argv)
    mainWindow = Dr_MainWindow()
    sys.exit(app.exec())
