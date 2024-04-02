import sys
from PySide6.QtCore import Qt, QSize, QRect, QUrl
from PySide6.QtGui import QIcon, QFont, QPainter, QPixmap, QPageSize, QDesktopServices, QPdfWriter, QFontMetrics
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QGridLayout, QCheckBox, \
    QLabel, QWidget, QLineEdit, QHBoxLayout, QFileDialog


from Datbase_Setting import search_medicine_data, SearchStartUpMedicine, get_medicine_id, get_dr_id_from_email, \
    add_to_favorite, load_favorite_medicines, delete_from_favorite, get_medicine_info
from Utilities import *
from datetime import datetime
import Authentication

from PySide6.QtWidgets import QMainWindow
from Final_Main_ui import Ui_Dr_MainWindow  # Update the import statement

class Dr_MainWindow(QMainWindow, Ui_Dr_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # Setup the user interface
        self.clear_scroll_area_2()  # Clear scroll area if needed
        self.favorite_state = {}
        self.favorite_medicines = []
        self.Selected_Medicine = []

        # Connect signals to slots
        self.pushButton_13.clicked.connect(self.Create_Prescription)
        self.Print_button.clicked.connect(self.Print)
        self.menuBtn.clicked.connect(self.CenterMenuPages)
        self.notificationBtn.clicked.connect(self.Notification)
        self.homeBtn.clicked.connect(self.HomePage)
        self.orderBtn.clicked.connect(self.OrderPage)
        self.reportsBtn.clicked.connect(self.ReportsPage)
        self.lineEdit_9.textEdited.connect(self.Search)

        # Initialize UI elements and flags
        self.centerMenuContatiner.hide()
        self.popupNotificationSubContainer.hide()
        self.menuBtn_Flag = True
        self.notificationBtn_Flag = True
        self.mainPages.setCurrentWidget(self.homePage)
        self.rightMenuSubContainer.show()
        self.FreezeColor("homeBtn")

        # Load data or perform any other necessary setup steps
        self.StartUpMedicine()
        self.load_favorite_data()

        # Show the main window
        self.show()


    def show_ui(self):
        self.show()

    def load_favorite_data(self):
        print("Welcome")
        email = Authentication.mail
        print(Authentication.mail)
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


        email = Authentication.mail
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
        text = self.lineEdit_9.text()
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

        scroll_layout1 = self.scrollArea_3.layout()

        if scroll_layout1 is None:
            scroll_layout1 = QVBoxLayout()
            self.scrollArea_3.setLayout(scroll_layout1)

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
        scroll_content1 = self.scrollArea_3.widget()

        # Clear existing layout and widgets
        if scroll_content1 is not None:
            # Remove the content widget from the scroll area
            self.scrollArea_3.takeWidget()

            # Delete the content widget
            scroll_content1.deleteLater()

    def Create_Prescription(self):
        self.OrderPage()

        # Clear the scroll area before adding new widgets
        self.clear_scroll_area3()

        # Add widgets to the scroll area
        self.add_widgets_to_scrollarea3()

    def Print(self):
        original_stylesheet = self.orderPage.styleSheet()
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
        self.orderPage.resize(frame_width_pixels, frame_height_pixels)

        self.Edite.hide()
        # self.pushButton_Trash.resize(0)
        self.Print_Frame.hide()
        self.label_29.setText(datetime.now().strftime('%d/%m/%y'))

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

        self.orderPage.setStyleSheet(font_stylesheet)

        # Create a pixmap to render the OrderPage widget onto it
        pixmap = QPixmap(self.orderPage.size())
        pixmap.fill(Qt.white)  # Fill pixmap with white background
        self.orderPage.render(pixmap)

        # Draw the pixmap onto the PDF
        painter.drawPixmap(0, 0, pixmap)

        # Close the painter
        painter.end()

        # Open the PDF file using a PDF viewer
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_filename))

        self.Edite.show()
        # self.pushButton_Trash.resize(0)
        self.Print_Frame.show()
        self.orderPage.setStyleSheet(original_stylesheet)

    def AddFrames(self, search_results):
        self.scrollArea.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_content.setLayout(self.scroll_layout)

        frame_count = len(search_results)
        rows = (frame_count + 2) // 3

        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.scroll_layout.addLayout(grid_layout)

        scroll_width = self.scrollArea.viewport().size().width()
        card_width = scroll_width // 3

        for i, result in enumerate(search_results):
            english_name = result['English_Name']
            medicine_price = result['Medicine_Price']
            active_substance = result['Active_Substance']
            frame = self.create_frame(english_name, medicine_price, active_substance)
            row = i // 3
            col = i % 3
            grid_layout.addWidget(frame, row, col)

        self.scrollArea.setWidget(self.scroll_content)

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

        if (english_name) in self.Selected_Medicine:
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
        self.drid = get_dr_id_from_email(Authentication.mail)
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

        if (english_name) in self.Selected_Medicine:
            checkBox.setChecked(True)

        checkBox.clicked.connect(
            lambda checked: self.checkbox_clicked_favorite(checked, english_name, active_substance))

        return frame

    def checkbox_clicked_favorite(self, checked, english_name, active_substance):
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

        # self.update_main_frames_favorite_state()
        # self.toggle_favorite(english_name,active_substance,None)
        # Update UI to remove the frame of the removed medicine
        frame.deleteLater()

        # Update favorite medicines in the database
        self.drid = get_dr_id_from_email(Authentication.mail)
        self.mid = get_medicine_id(english_name, active_substance)
        delete_from_favorite(self.drid, self.mid)
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
        self.scrollArea_2.setWidget(widget)

    def clear_scroll_area_2(self):
        if self.scrollArea_2.layout() is not None:
            for i in reversed(range(self.scrollArea_2.layout().count())):
                widget = self.scrollArea_2.layout().itemAt(i).widget()
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






