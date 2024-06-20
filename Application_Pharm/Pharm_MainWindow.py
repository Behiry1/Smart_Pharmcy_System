from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton, QSpinBox, \
    QSizePolicy, QGridLayout, QFrame,QScrollArea
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt, QDateTime

import Authentication
from Pharm_MainWindow_Database import get_prescription_details, insert_receipt_and_details, get_receipt_details,get_receipt_details_info,get_specific_medicines_details
from Pharm_mainwindow_ui import Ui_MainWindow
from functools import partial  # Import partial
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QFrame, QLabel, QCheckBox
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QCheckBox, QFrame, QApplication, QMainWindow, QScrollArea, QHBoxLayout
from PySide6.QtCore import Qt
import sys
from Request_Medicines import *



class Pharm_Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.StartUp_Pharmwindow()



    def StartUp_Pharmwindow(self):

        self.setupUi(self)
        self.Clear_prescription_Scrollarea6()

        self.show()

        self.menuBtn.clicked.connect(self.CenterMenuPages)
        self.notificationBtn.clicked.connect(self.Notification)
        self.homeBtn.clicked.connect(self.HomePage)
        self.orderBtn.clicked.connect(self.OrderPage)
        self.reportsBtn.clicked.connect(self.ReportsPage)
        self.pushButton.clicked.connect(self.AiPage)

        self.centerMenuContatiner.hide()
        self.popupNotificationSubContainer.hide()
        self.menuBtn_Flag = True
        self.notificationBtn_Flag = True
        self.mainPages.setCurrentWidget(self.homePage)
        self.rightMenuSubContainer.show()
        self.FreezeColor("homeBtn")

        self.pushButton_23.clicked.connect(self.Search_Prescription)
        self.ADD_To_Machine.clicked.connect(self.SendMachine)

        # Setup the scroll area
        self.scrollAreaWidgetContents_6.setLayout(QVBoxLayout())
        self.total_sum = 0.0
        self.medicine_list = []
        self.receipt_Data = []
        self.Clear_prescription_Scrollarea4()
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setLayout(QGridLayout())
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.Clear_prescription_Scrollarea4()
        self.get_receipt_details_from_database()
        self.lineEdit_11.textChanged.connect(self.Search_Receipt)
        medicines = get_specific_medicines_details()
        self.scrollAreaWidgetContents_5 = QWidget()  # Initialize the widget container
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)  # Set content wid
        self.add_medicine_frames(medicines)
    def Search_Prescription(self):
        self.lineEdit_9.setStyleSheet("")
        # Get the prescription ID from the QLineEdit
        prescription_id = self.lineEdit_9.text().strip()

        if not prescription_id.isdigit():
            print("Invalid Prescription ID")
            return

        # Call the get_prescription_details function
        medicines, dr_name, prescription_date,flag = get_prescription_details(int(prescription_id))
        print(flag)
        print(medicines)
        if flag == 1:
            self.lineEdit_9.setStyleSheet("color: red;")
            self.lineEdit_9.setText("It has been disbursed before")
            self.Clear_prescription_Scrollarea6()
            self.Doctor_Name.setText("Dr: ")
            self.Date.setText("Date")
            self.lineEdit_9.clear()
            return

        if not dr_name:
            self.Clear_prescription_Scrollarea6()
            self.Doctor_Name.setText("Dr: ")
            self.Date.setText("Date")
            self.lineEdit_9.clear()
            self.lineEdit_9.setStyleSheet("color: red;")
            self.lineEdit_9.setText("Enter a valid prescription ID")
            return
        self.Doctor_Name.setText("Dr: " + str(dr_name))
        self.Date.setText(str(prescription_date))

        # Clear previous results
        layout = self.scrollAreaWidgetContents_6.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Add new medicine widgets
        self.Edite_3.show()
        self.ADD_To_Machine.show()
        self.medicine_list.clear()

        for medicine in medicines:
            self.add_medicine_widget(medicine)

    def Search_Receipt(self):
        search_info = self.lineEdit_11.text().strip()
        receipt_data = get_receipt_details(search_info)
        self.Clear_prescription_Scrollarea4()
        self.add_frames_from_receipt_details(receipt_data)

    def add_medicine_frames(self, medicines):


            if not medicines:
                print("No medicines provided to add.")
                return

            # Create a grid layout for the container widget
            grid_layout = QGridLayout()
            grid_layout.setSpacing(10)  # Add some spacing between the frames

            for index, medicine in enumerate(medicines):
                # Create a frame for each medicine
                frame = QFrame()
                frame.setObjectName(f"Cared_{index + 1}")  # Unique object name for each frame

                # Apply style sheet to only color the borders
                frame.setStyleSheet(f"QFrame#Cared_{index + 1} {{ border: 2px solid #265c36; border-radius: 5px; }}")

                frame.setFrameShape(QFrame.StyledPanel)
                frame.setFrameShadow(QFrame.Raised)
                frame.setFixedSize(550, 120)  # Fixed size for the frame

                # Create a layout for the frame
                frame_layout = QVBoxLayout(frame)
                frame_layout.setContentsMargins(5, 5, 5, 5)  # Adjust margins for better spacing
                frame_layout.setSpacing(5)

                # Extract details from the medicine dictionary
                medicine_name = medicine.get('English_Name', 'N/A')
                active_substance = medicine.get('Active_Substance', 'N/A')
                price = float(medicine.get('Price', 0.0))  # Default to 0.0 if no price provided

                # Create a checkbox for selecting the medicine
                checkbox = QCheckBox("Select")
                checkbox.setObjectName(f"checkBox_{index + 1}")  # Unique object name for each checkbox
                checkbox.setChecked(False)  # Initially unchecked
                checkbox.stateChanged.connect(lambda state, idx=index: self.checkbox_state_changed(state, idx))
                frame_layout.addWidget(checkbox)  # Add checkbox to the frame layout

                # Create horizontal layouts for each label and value pair
                row_layout1 = QHBoxLayout()
                label_name_text = QLabel("English Name:")
                label_name_value = QLabel(medicine_name)
                row_layout1.addWidget(label_name_text)
                row_layout1.addWidget(label_name_value)
                frame_layout.addLayout(row_layout1)  # Add the row layout to the frame

                row_layout2 = QHBoxLayout()
                label_price_text = QLabel("Price:")
                label_price_value = QLabel(f"{price:.2f}")
                row_layout2.addWidget(label_price_text)
                row_layout2.addWidget(label_price_value)
                frame_layout.addLayout(row_layout2)  # Add the row layout to the frame

                row_layout3 = QHBoxLayout()
                label_active_substance_text = QLabel("Active Substance:")
                label_active_substance_value = QLabel(active_substance)
                row_layout3.addWidget(label_active_substance_text)
                row_layout3.addWidget(label_active_substance_value)
                frame_layout.addLayout(row_layout3)  # Add the row layout to the frame

                # Add the frame to the main grid layout
                grid_layout.addWidget(frame, index // 3, index % 3)  # Distribute frames in rows and columns

            # Set the new grid layout to scrollAreaWidgetContents_5
            self.scrollAreaWidgetContents_5.setLayout(grid_layout)

            # Debug print to confirm function execution
            print("Medicine frames added successfully.")


    def clear_layout(self, layout):


        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def checkbox_state_changed(self, state, index):

            checkbox = self.findChild(QCheckBox, f"checkBox_{index + 1}")
            if checkbox:
                if state == Qt.Checked:
                    print(f"Checkbox {index + 1} selected.")
                    # Perform actions when the checkbox is selected
                else:
                    print(f"Checkbox {index + 1} deselected.")
                    # Perform actions when the checkbox is deselected

    def add_medicine_widget(self, medicine, l=None):
        if l is not None:
            self.Doctor_Name.setText("Dr: " + str(l.get("Doctor_Name",'')))
            self.Date.setText(str(l.get("Receipt_Date",'')))

            self.Edite_3.hide()
            self.ADD_To_Machine.hide()

            for med in medicine:


                # Create a new widget for the medicine details
                widget = QWidget()
                layout = QHBoxLayout(widget)

                # Set properties similar to your provided UI XML
                widget.setMinimumSize(0, 30)
                widget.setMaximumSize(16777215, 30)
                widget.setStyleSheet("QLabel, QSpinBox{"
                                     "border-left: 1px solid #1fc150;"
                                     "color: black;"
                                     "qproperty-alignment: AlignCenter;"
                                     "border-right: 0px solid #1fc150;"
                                     "}"
                                     "QPushButton {"
                                     "border-left: 1px solid #1fc150;"
                                     "background-color: rgb(38, 92, 54);"
                                     "border-radius: 10px;"
                                     "border-right: 0px solid #1fc150;"
                                     "}"
                                     "* {"
                                     "border-bottom: 1px solid #1fc150;"
                                     "border-top: 1px solid #1fc150;"
                                     "}")

                # Extract medicine details from dictionary
                medicine_name = med.get('Medicine_Name', '')
                medicine_count = med.get('Number_of_units', 1)  # Correct key name to 'Number_of_units'
                medicine_usage = med.get('Medicine_Usage', '')
                medicine_price = float(med.get('Price', 0.0))  # Ensure price is a float
                medicine_x = med.get('loc_x','')
                medicine_y = med.get('loc_y','')

                # Calculate the total price
                total_price = medicine_price * medicine_count

                # Create labels
                label_name = QLabel(medicine_name)
                label_name.setMinimumSize(220, 30)
                label_name.setFont(QFont("Segoe UI", 9))
                label_name.setAlignment(Qt.AlignCenter)
                label_name.setObjectName("label_name")

                label_usage = QLabel(medicine_usage)
                label_usage.setMinimumSize(210, 30)
                label_usage.setFont(QFont("Segoe UI", 9))
                label_usage.setAlignment(Qt.AlignCenter)
                label_usage.setObjectName("label_usage")

                label_price = QLabel(f"{total_price:.2f}")  # Display the total price
                label_price.setMinimumSize(50, 30)
                label_price.setMaximumSize(150, 16777215)
                label_price.setFont(QFont("Segoe UI", 9))
                label_price.setAlignment(Qt.AlignCenter)
                label_price.setObjectName("label_price")

                label_count = QLabel(str(medicine_count))
                label_count.setMinimumSize(50, 30)
                label_count.setMaximumSize(120, 30)
                label_count.setFont(QFont("Segoe UI", 10))
                label_count.setAlignment(Qt.AlignCenter)
                label_count.setObjectName("label_count")

                # Add widgets to layout
                layout.addWidget(label_name)
                layout.addWidget(label_usage)
                layout.addWidget(label_price)
                layout.addWidget(label_count)

                # Ensure layout margins are set to 0 to match the style
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)

                # Add the widget to the scroll area's layout
                self.scrollAreaWidgetContents_6.layout().addWidget(widget)

            return
        else:
            # Create a new widget for the medicine details
            widget = QWidget()
            layout = QHBoxLayout(widget)

            # Set properties similar to your provided UI XML
            widget.setMinimumSize(0, 30)
            widget.setMaximumSize(16777215, 30)
            widget.setStyleSheet("QLabel, QSpinBox{"
                                 "border-left: 1px solid #1fc150;"
                                 "color: black;"
                                 "qproperty-alignment: AlignCenter;"
                                 "border-right: 0px solid #1fc150;"
                                 "}"
                                 "QPushButton {"
                                 "border-left: 1px solid #1fc150;"
                                 "background-color: rgb(38, 92, 54);"
                                 "border-radius: 10px;"
                                 "border-right: 0px solid #1fc150;"
                                 "}"
                                 "* {"
                                 "border-bottom: 1px solid #1fc150;"
                                 "border-top: 1px solid #1fc150;"
                                 "}")

            # Extract medicine details
            medicine_name = medicine.get('Medicine_Name', '')
            medicine_usage = medicine.get('Medicine_Usage', '')
            medicine_price = float(medicine.get('Medicine_Price', 0.0))  # Ensure price is a float
            medicine_count = int(medicine.get('Medicine_Count', 1))  # Ensure count is an integer
            medicine_x = medicine.get('loc_x', '')
            medicine_y = medicine.get('loc_y', '')

            # Calculate the total price
            total_price = medicine_price * medicine_count

            # Create labels and spin box
            label_name = QLabel(medicine_name)
            label_name.setMinimumSize(220, 30)
            label_name.setFont(QFont("Segoe UI", 9))
            label_name.setAlignment(Qt.AlignCenter)
            label_name.setObjectName("label_name")

            label_usage = QLabel(medicine_usage)
            label_usage.setMinimumSize(210, 30)
            label_usage.setFont(QFont("Segoe UI", 9))
            label_usage.setAlignment(Qt.AlignCenter)
            label_usage.setObjectName("label_usage")

            label_price = QLabel(f"{total_price:.2f}")  # Display the total price
            label_price.setMinimumSize(50, 30)
            label_price.setMaximumSize(150, 16777215)
            label_price.setFont(QFont("Segoe UI", 9))
            label_price.setAlignment(Qt.AlignCenter)
            label_price.setObjectName("label_price")

            spin_box_count = QSpinBox()
            spin_box_count.setMinimum(1)
            spin_box_count.setMaximum(medicine_count)
            spin_box_count.setValue(medicine_count)
            spin_box_count.setMinimumSize(50, 30)
            spin_box_count.setMaximumSize(120, 30)
            spin_box_count.setFont(QFont("Segoe UI", 10))
            spin_box_count.setAlignment(Qt.AlignCenter)
            spin_box_count.valueChanged.connect(
                lambda value, label=label_price, price=medicine_price: self.update_total(label, value, price))

            button_trash = QPushButton()
            button_trash.setMaximumSize(50, 30)
            button_trash.setIcon(QIcon(":/Icon_web/Image_for_main/icons_from_Web/trash-2.svg"))
            button_trash.clicked.connect(lambda: self.remove_medicine_widget(widget, label_price))

            # Add widgets to layout
            layout.addWidget(label_name)
            layout.addWidget(label_usage)
            layout.addWidget(label_price)
            layout.addWidget(spin_box_count)
            layout.addWidget(button_trash)

            # Ensure layout margins are set to 0 to match the style
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)

            # Add the widget to the scroll area's layout
            self.scrollAreaWidgetContents_6.layout().addWidget(widget)

            # Extract medicine details for the medicine list
            self.medicine_list.append({
                "Medicine_Name": medicine_name,
                "Count": medicine_count,
                "Price_Per_Count": medicine_price,
                "loc_x": medicine_x,
                "loc_y": medicine_y
            })

            # Update the total sum
            self.update_total_sum()
    def update_total(self, label, value, price):
        # Update the label with the new total price
        new_total = value * price
        label.setText(f"{new_total:.2f}")

        # Update the count in the medicine_list
        medicine_name = label.parent().findChild(QLabel, "label_name").text()
        for med_info in self.medicine_list:
            if med_info["Medicine_Name"] == medicine_name:
                med_info["Count"] = value
                break

        # Update the total sum
        self.update_total_sum()
    def get_receipt_details_from_database(self):
        # This function retrieves receipt details from the database
        receipt_details = get_receipt_details()
        self.add_frames_from_receipt_details(receipt_details)

    def add_frames_from_receipt_details(self, receipt_details):
        # This function adds frames to scrollArea_4 based on the receipt details
        # Clear existing frames
        self.Clear_prescription_Scrollarea4()

        # Add frames for each receipt entry
        for receipt in receipt_details:
            prescription_id = receipt["Prescription_ID"]
            dr_name = receipt["Dr_Name"]
            prescription_date = receipt["Date"]
            total_price = receipt["Total_Price"]

            # Create a frame for the receipt entry
            frame = QFrame()
            frame.setFixedSize(420, 100)  # Fixed size for the frame
            frame.setStyleSheet("#pushButton_8{background-color: #265c36;}")
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)

            label_prescription_id = QLabel("Prescription id:")
            label_prescription_id.setMinimumSize(110, 0)

            label_prescription_id_value = QLabel(str(prescription_id))
            label_prescription_id_value.setMinimumSize(110, 0)

            label_doctor_name = QLabel("Doctor Name:")
            label_doctor_name_value = QLabel(dr_name)

            label_date_time = QLabel("Date & Time:")
            label_date_time_value = QLabel(
                QDateTime.fromString(str(prescription_date), "yyyy-MM-dd").toString("yyyy-MM-dd HH:mm"))

            label_total_price = QLabel("Total Price:")
            label_total_price_value = QLabel(str(total_price))

            pushButton_details = QPushButton("Details")
            pushButton_details.setMinimumSize(70, 24)
            pushButton_details.setMaximumSize(50, 24)
            pushButton_details.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Set fixed size policy
            pushButton_details.setFont(QFont("", 9))
            pushButton_details.setIcon(QIcon(":/Icon_web/Image_for_main/icons_from_Web/external-link.svg"))

            # Connect the clicked signal of the button to a custom slot function
            pushButton_details.clicked.connect(partial(self.show_prescription_details, prescription_id))

            grid_layout = QGridLayout(frame)
            grid_layout.addWidget(label_prescription_id, 0, 0)
            grid_layout.addWidget(label_prescription_id_value, 0, 1, 1, 2)
            grid_layout.addWidget(label_doctor_name, 1, 0)
            grid_layout.addWidget(label_doctor_name_value, 1, 1)
            grid_layout.addWidget(label_date_time, 2, 0)
            grid_layout.addWidget(label_date_time_value, 2, 1)
            grid_layout.addWidget(pushButton_details, 2, 2, 2, 1)
            grid_layout.addWidget(label_total_price, 3, 0)
            grid_layout.addWidget(label_total_price_value, 3, 1)

            grid_layout.setColumnStretch(0, 1)
            grid_layout.setColumnStretch(1, 2)
            grid_layout.setColumnStretch(2, 1)

            # Add the frame to the scroll area
            grid_layout_scroll_area = self.scrollAreaWidgetContents_4.layout()
            row = self.frame_counter // 4  # 4 frames per row
            col = self.frame_counter % 4  # 4 frames per row
            grid_layout_scroll_area.addWidget(frame, row, col)
            self.frame_counter += 1

    def show_prescription_details(self, prescription_id):
        self.HomePage()
        self.Clear_prescription_Scrollarea6()
        dr_info,medicine_data = get_receipt_details_info(prescription_id)
        print(medicine_data)
        self.add_medicine_widget(medicine_data,dr_info)


    def Clear_prescription_Scrollarea4(self):

        grid_layout = self.scrollAreaWidgetContents_4.layout()
        while grid_layout.count():
            child = grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.frame_counter = 0
    def remove_medicine_widget(self, widget, label_price):
        # Remove the widget from the layout
        widget.setParent(None)

        # Remove the corresponding medicine details from the medicine list
        index_to_remove = None
        for index, med_info in enumerate(self.medicine_list):
            if med_info["Medicine_Name"] == label_price.parent().findChild(QLabel, "label_name").text():
                index_to_remove = index
                break
        if index_to_remove is not None:
            del self.medicine_list[index_to_remove]

        # Update the total sum
        self.update_total_sum()
    def update_total_sum(self):
        total_sum = 0.0
        layout = self.scrollAreaWidgetContents_6.layout()

        # Iterate through all widgets in the layout and sum the prices
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                label_price = widget.findChild(QLabel, "label_price")
                if label_price:
                    try:
                        total_sum += float(label_price.text())
                    except ValueError:
                        pass  # Ignore labels that do not contain valid float values

        # Update the global total sum
        self.total_sum = total_sum
        print(self.total_sum)

    def Clear_prescription_Scrollarea6(self):
        self.Doctor_Name.setText("Dr: ")
        self.Date.setText("Date")
        self.lineEdit_9.clear()

        layout = self.scrollAreaWidgetContents_6.layout()
        if layout is not None:
            while layout.count():
                widget = layout.takeAt(0).widget()
                if widget is not None:
                    widget.deleteLater()
        self.total_sum = 0.0

    def SendMachine(self):
        prescription_id = self.lineEdit_9.text().strip()  # Replace with the actual prescription ID
        total_price = self.total_sum  # Assuming total_sum is already calculated
        pharm_id = Authentication.Pharm_id  # Replace with the actual pharmacy ID
        receipt_date = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm")  # Get current date in ISO format

        # Create a list to store the prescription details
        prescription_details = [(prescription_id, pharm_id, receipt_date, total_price)]

        # Create a list to store the medicine details
        medicine_details = []
        medicine_path = []
        for medicine in self.medicine_list:
            medicine_name = medicine["Medicine_Name"]
            count = medicine["Count"]
            price_per_count = medicine["Price_Per_Count"]
            location_x = medicine["loc_x"]
            location_y = medicine["loc_y"]

            # Append details as a tuple to medicine_details
            medicine_details.append((medicine_name, count, price_per_count))

            # Append details as a dictionary to medicine_path
            medicine_path.append({
                'Medicine_Name': medicine_name,
                'Count': count,
                'Price_Per_Count': price_per_count,
                'loc_x': location_x,
                'loc_y': location_y
            })

        print(medicine_path)

        # Call the insert_receipt_and_details function with the formatted data
        astar_grid = AStarGrid()
        steps = astar_grid.find_steps_from_input(medicine_path)
        insert_receipt_and_details(prescription_details, medicine_details)
        self.Doctor_Name.setText("Dr: ")
        self.Date.setText("Date")
        self.lineEdit_9.clear()

        # Clear the prescription scroll area
        self.Clear_prescription_Scrollarea6()
        self.get_receipt_details_from_database()

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
        self.ClearBackGround_Color("pushButton")
    def OrderPage(self):
        self.mainPages.setCurrentWidget(self.reportsPage)
        self.rightMenuSubContainer.hide()
        self.FreezeColor("orderBtn")
        self.ClearBackGround_Color("reportsBtn")
        self.ClearBackGround_Color("homeBtn")
        self.ClearBackGround_Color("pushButton")
    def ReportsPage(self):
        self.mainPages.setCurrentWidget(self.orderPage)
        self.rightMenuSubContainer.hide()
        self.FreezeColor("reportsBtn")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("homeBtn")
        self.ClearBackGround_Color("pushButton")
    def AiPage(self):
        self.mainPages.setCurrentWidget(self.AI)
        self.rightMenuSubContainer.hide()
        self.FreezeColor("pushButton")
        self.ClearBackGround_Color("orderBtn")
        self.ClearBackGround_Color("homeBtn")
        self.ClearBackGround_Color("reportsBtn")
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
            self.pushButton,
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
            self.pushButton,
        ]
        for btn in self.buttons:
            if btn.objectName() == button:
                btn.setStyleSheet("background-color: transparent")
                btn.setStyleSheet("QPushButton:hover {background-color:rgb(28, 171, 213)}")
