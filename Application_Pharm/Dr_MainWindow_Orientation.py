from datetime import datetime

from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QFont, QIcon, Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QFrame, QGridLayout, QLabel, QCheckBox, QPushButton, QHBoxLayout, \
    QLineEdit, QSpinBox

import Authentication

from Dr_MainWindow_Database import delete_from_favorite, get_dr_id_from_email, get_medicine_id, add_to_favorite, \
    get_medicine_info, get_Pr_medicine_id, load_prescription_details, retrieve_medicine_info


class Favorite_Orientation:
    @staticmethod
    def display_favorite_medicines(ui):
        Favorite_Orientation.clear_scroll_area_2(ui)

        layout = QVBoxLayout()
        for name, substance in ui.favorite_medicines:
            frame = Favorite_Orientation.create_favorite_frame(ui,name, substance)
            layout.addWidget(frame)

        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)
        ui.scrollArea_2.setWidget(widget)

    @staticmethod
    def remove_from_favorites(ui, english_name, active_substance, frame,favorite_medicines,favorite_state):
        # Remove medicine from the favorite list
        favorite_medicines.remove((english_name, active_substance))
        favorite_state[(english_name, active_substance)] = False

        # self.update_main_frames_favorite_state()
        # self.toggle_favorite(english_name,active_substance,None)
        # Update UI to remove the frame of the removed medicine
        frame.deleteLater()

        # Update favorite medicines in the database
        drid = get_dr_id_from_email(Authentication.mail)
        mid = get_medicine_id(english_name, active_substance)
        delete_from_favorite(drid, mid)
        ui.Search()

    @staticmethod
    def create_favorite_frame(ui, english_name, active_substance):
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
        pushButton.clicked.connect(lambda: Favorite_Orientation.remove_from_favorites(ui,english_name, active_substance, frame,ui.favorite_medicines,ui.favorite_state))

        if (english_name) in ui.Selected_Medicine:
            checkBox.setChecked(True)

        checkBox.clicked.connect(
            lambda checked: Favorite_Orientation.checkbox_clicked_favorite(ui,checked, english_name, active_substance,ui.Selected_Medicine))

        return frame

    @staticmethod
    def checkbox_clicked_favorite(ui, checked, english_name, active_substance, Selected_Medicine):
        if checked:
            # Checkbox is checked
            print(f"{english_name} with active substance {active_substance} is selected.")
            # Add the English name of the selected medicine to the Selected_Medicine array
            Selected_Medicine.append(english_name)
            # Perform certain function here (if needed)
        else:
            # Checkbox is unchecked
            print(f"{english_name} with active substance {active_substance} is deselected.")
            # Remove the English name of the deselected medicine from the Selected_Medicine array (if it exists)
            if english_name in Selected_Medicine:
                Selected_Medicine.remove(english_name)
            # Perform certain function here (if needed)
        print(Selected_Medicine)
        ui.Search()

    @staticmethod
    def clear_scroll_area_2(ui):
        if ui.scrollArea_2.layout() is not None:
            for i in reversed(range(ui.scrollArea_2.layout().count())):
                widget = ui.scrollArea_2.layout().itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()

    @staticmethod
    def toggle_favorite(ui, english_name, active_substance, button, favorite_medicines, favorite_state):
        if (english_name, active_substance) not in favorite_state:
            favorite_state[(english_name, active_substance)] = True
            favorite_medicines.append((english_name, active_substance))
            button.setStyleSheet(
                "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
        else:
            favorite_state[(english_name, active_substance)] = not favorite_state[(english_name, active_substance)]

            if favorite_state[(english_name, active_substance)]:
                favorite_medicines.append((english_name, active_substance))
                button.setStyleSheet(
                    "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")
            else:
                if (english_name, active_substance) in favorite_medicines:
                    favorite_medicines.remove((english_name, active_substance))
                button.setStyleSheet("max-width: 30px;min-height:20px")  # Reset style to default

        medicine_ids = [get_medicine_id(name, substance) for name, substance in favorite_medicines]

        Favorite_Orientation.display_favorite_medicines(ui)

        ui.drid = get_dr_id_from_email(Authentication.mail)
        add_to_favorite(ui.drid, medicine_ids)

    @staticmethod
    def favorite_action(english_name, active_substance, favorite_medicines):
        print(f"{english_name} with active substance {active_substance} favorited")
        print(favorite_medicines)

    @staticmethod
    def unfavorite_action(english_name, active_substance):
        print(f"{english_name} with active substance {active_substance} unfavorited")
class MainPages_Orientation:


    @staticmethod
    def AddFrames(ui, search_results):
        ui.scrollArea.setWidgetResizable(True)
        ui.scroll_content = QWidget()
        ui.scroll_layout = QVBoxLayout()
        ui.scroll_content.setLayout(ui.scroll_layout)

        frame_count = len(search_results)
        rows = (frame_count + 2) // 3

        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        ui.scroll_layout.addLayout(grid_layout)

        scroll_width = ui.scrollArea.viewport().size().width()
        card_width = scroll_width // 3

        for i, result in enumerate(search_results):
            english_name = result['English_Name']
            medicine_price = result['Medicine_Price']
            active_substance = result['Active_Substance']
            frame = MainPages_Orientation.create_Medicine_frame(ui, english_name, medicine_price, active_substance)
            row = i // 3
            col = i % 3
            grid_layout.addWidget(frame, row, col)

        ui.scrollArea.setWidget(ui.scroll_content)

    @staticmethod
    def create_Medicine_frame(ui, english_name, medicine_price, active_substance):
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
        if (english_name, active_substance) in ui.favorite_state:
            if ui.favorite_state[(english_name, active_substance)]:
                button.setStyleSheet(
                    "max-width: 30px;min-height:20px;border: 0px solid black;background-image:url(:/Icon_custom/Image_for_main/icon_custom/red_heart.png);background-position: center;background-repeat: no-repeat;")

        button.clicked.connect(lambda: Favorite_Orientation.toggle_favorite(ui, english_name, active_substance, button,
                                                                          ui.favorite_medicines, ui.favorite_state))

        if (english_name) in ui.Selected_Medicine:
            select_checkbox.setChecked(True)

        # Connect the clicked signal of the checkbox to the checkbox_clicked slot function
        select_checkbox.clicked.connect(
            lambda checked: MainPages_Orientation.checkbox_clicked(ui,checked, english_name, active_substance))

        return frame

    @staticmethod
    def Clear_Medicine_Frames(ui):
        ui.scroll_content = QWidget()
        # self.scroll_area.setWidgetResizable(True)
        ui.scroll_layout = QGridLayout(ui.scroll_content)
        # Remove all existing frames from the scroll area
        for i in reversed(range(ui.scroll_layout.count())):
            widget = ui.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    @staticmethod
    def checkbox_clicked(ui, checked, english_name, active_substance):
        if checked:
            # Checkbox is checked
            print(f"{english_name} with active substance {active_substance} is selected.")
            # Add the English name of the selected medicine to the Selected_Medicine array
            ui.Selected_Medicine.append(english_name)
            # Perform certain function here (if needed)
        else:
            # Checkbox is unchecked
            print(f"{english_name} with active substance {active_substance} is deselected.")
            # Remove the English name of the deselected medicine from the Selected_Medicine array (if it exists)
            if english_name in ui.Selected_Medicine:
                ui.Selected_Medicine.remove(english_name)
            # Perform certain function here (if needed)
        print(ui.Selected_Medicine)
        Favorite_Orientation.display_favorite_medicines(ui)
class Prescription_Orientation:
    @staticmethod
    def Create_Prescription(ui):
        ui.label_29.setText(datetime.now().strftime('%y/%m/%d'))
        ui.label_28.setText(Authentication.Dept)
        ui.label_31.setText(Authentication.name)

        ui.OrderPage()

        # Clear the scroll area before adding new widgets
        Prescription_Orientation.Clear_Prescription_Page(ui)

        # Add widgets to the scroll area
        Prescription_Orientation.Add_To_Prescription_Page(ui)

    @staticmethod
    def create_prescription_widget(ui, medicine_info):
        Prescription_Orientation.Clear_Prescription_Page(ui)

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

        # Count QSpinBox
        count_spinbox = QSpinBox()
        count_spinbox.setObjectName("count")
        count_spinbox.setMinimum(1)  # Set minimum value
        count_spinbox.setMaximum(9999)  # Set maximum value
        count_spinbox.setValue(1)  # Set default value
        count_spinbox.setMinimumSize(50, 35)
        count_spinbox.setMaximumSize(120, 35)
        count_spinbox.setFont(QFont())
        inner_layout.addWidget(count_spinbox)

        # Connect count spinbox's valueChanged signal to update_price_label function
        count_spinbox.valueChanged.connect(
            lambda value: Prescription_Orientation.update_price_label(count_spinbox, price,
                                                                      float(medicine_info.get('Medicine_Price', 0))))

        # Delete Button
        delete_button = QPushButton()
        delete_button.setMaximumSize(35, 35)
        delete_button.setIcon(QIcon(":/Icon_web/Image_for_main/icons_from_Web/trash-2.svg"))
        delete_button.setStyleSheet("background-color: rgb(255, 34, 34); border-radius: 10px;")
        inner_layout.addWidget(delete_button)

        # Connect delete button clicked signal to delete_widget function
        delete_button.clicked.connect(lambda: Prescription_Orientation.delete_widget(ui, ui.scrollArea, widget,
                                                                                     medicine_info.get('English_Name',
                                                                                                       'N/A')))

        frame.setLayout(inner_layout)
        layout.addWidget(frame)

        widget.setLayout(layout)

        # Apply stylesheet to the widget container and its child labels
        # widget.setStyleSheet("""
        #     QLabel {
        #         border-left: 1px solid #064666;
        #         qproperty-alignment: 'AlignCenter';
        #         border-right: 0px solid #064666;
        #     }
        #
        #     QPushButton {
        #         background-color: rgb(255, 34, 34);
        #         border-radius: 10px;
        #     }
        #
        #     * {
        #         border-bottom: 1px solid #064666;
        #         border-top: 1px solid #064666;
        #     }
        # """)

        # Ensure that the scroll area has a layout set
        if not ui.scrollArea.layout():
            scroll_layout = QVBoxLayout()
            ui.scrollArea.setLayout(scroll_layout)

        # Add the widget to the scroll area layout
        ui.scrollArea.layout().addWidget(widget)

        return widget

    @staticmethod
    def update_price_label(count_edit, price_label, medicine_price):
        count = count_edit.text()
        try:
            count = int(count)
        except ValueError:
            # Handle non-integer input gracefully
            count = 0
        total_price = count * medicine_price
        price_label.setText(str(total_price))

    @staticmethod
    def delete_widget(ui,scroll_area, widget,medicine_name):
        # Find the index of the widget in the layout
        index = scroll_area.layout().indexOf(widget)

        # Remove the widget from the layout
        scroll_area.layout().removeWidget(widget)

        # Delete the widget to release memory
        widget.deleteLater()
        print(f"{medicine_name} is deselected.")
        # Remove the English name of the deselected medicine from the Selected_Medicine array (if it exists)
        if medicine_name in ui.Selected_Medicine:
            ui.Selected_Medicine.remove(medicine_name)

        # Perform certain function here (if needed)
        print(ui.Selected_Medicine)
        Favorite_Orientation.display_favorite_medicines(ui)
        ui.Search()



    @staticmethod
    def Add_To_Prescription_Page(ui):
        scroll_layout = ui.scrollArea_3.layout()

        if scroll_layout is None:
            scroll_layout = QVBoxLayout()
            ui.scrollArea_3.setLayout(scroll_layout)

        existing_widgets = [scroll_layout.itemAt(i).widget() for i in range(scroll_layout.count())]

        for medicine_name in ui.Selected_Medicine:
            if any(widget.property("medicine_name") == medicine_name for widget in existing_widgets):
                continue

            # Retrieve medicine information from the database
            medicine_info = get_medicine_info(medicine_name)

            if medicine_info:
                # Create a widget using the retrieved information
                widget = Prescription_Orientation.create_prescription_widget(ui, medicine_info)
                widget.setProperty("medicine_name", medicine_name)  # Set custom property for medicine name

                # Add the widget to the scroll area
                widget.setFixedSize(16777215, 35)  # Set fixed size for the widget
                scroll_layout.addWidget(widget)  # Add widget to the layout
    @staticmethod
    def Clear_Prescription_Page(ui):
        # Get the scroll area's content widget
        scroll_content1 = ui.scrollArea_3.widget()

        # Clear existing layout and widgets
        if scroll_content1 is not None:
            # Remove the content widget from the scroll area
            ui.scrollArea_3.takeWidget()

            # Delete the content widget
            scroll_content1.deleteLater()

    @staticmethod
    def Clear_Prescription_Page1(ui):
        # Get the layout of the scroll area
        ui.label_32.clear()
        ui.Patient_name_lineEdit.clear()
        ui.Patient_name_lineEdit_2.clear()
        scroll_layout = ui.scrollArea_3.layout()

        # Clear existing widgets from the layout
        if scroll_layout is not None:
            while scroll_layout.count():
                item = scroll_layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        ui.Selected_Medicine.clear()
        Favorite_Orientation.display_favorite_medicines(ui)
        ui.Search()

    @staticmethod
    def get_medicine_counts(ui):
        scroll_layout = ui.scrollArea_3.layout()
        medicine_counts = []

        if scroll_layout is not None:
            for i in range(scroll_layout.count()):
                widget = scroll_layout.itemAt(i).widget()
                english_name = widget.property("medicine_name")
                print(english_name)

                # Find the QSpinBox for counting
                count_spinbox = widget.findChild(QSpinBox, "count")
                if count_spinbox is not None:
                    count = count_spinbox.value()
                    medicine_id = get_Pr_medicine_id(english_name)

                    # Append a tuple of (medicine_id, count) to the medicine_counts list
                    if medicine_id is not None:  # Make sure medicine_id is valid
                        medicine_counts.append((medicine_id, count))

        return medicine_counts

class History_Orientation:

    @staticmethod
    def create_history_widgets(ui, prescription_id, patient_name, prescription_date):
        # Create main widget
        widget = QWidget()
        widget.setWindowTitle("Sample Widget")
        widget.setFixedSize(16777215, 95)  # Set fixed size for the widget

        # Main layout
        main_layout = QVBoxLayout(widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align the layout to the top

        # Frame
        frame = QFrame()
        frame.setObjectName("Cared_10")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

        # Layout for frame
        layout = QGridLayout(frame)

        # Labels
        label1 = QLabel("Prescription id :")
        label1.setObjectName("prescription_id_label")  # Set unique object name
        label2 = QLabel("Patient Name :")
        label2.setObjectName("patient_name_label")  # Set unique object name
        label3 = QLabel("Date & Time :")
        label4 = QLabel(str(prescription_id))
        label5 = QLabel(patient_name)
        label6 = QLabel(str(prescription_date))

        # Push Button
        push_button = QPushButton("Show Details")
        push_button.setIcon(QIcon(":/Icon_web/Image_for_main/icons_from_Web/external-link.svg"))
        push_button.setMinimumSize(QSize(110, 24))
        push_button.setMaximumSize(QSize(157, 24))
        push_button.setFont(QFont("", 9))

        push_button.clicked.connect(lambda: History_Orientation.showDetails(ui,prescription_id))

        # Add widgets to layout
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(label4, 0, 1)
        layout.addWidget(label5, 1, 1)
        layout.addWidget(label6, 2, 1)
        layout.addWidget(push_button, 0, 2, 3, 1)

        # Add frame to main layout
        main_layout.addWidget(frame)

        return widget

    @staticmethod
    def showDetails(ui, pr_id):
        print(pr_id)
        Prescription_Orientation.Clear_Prescription_Page1(ui)
        medicine_info = retrieve_medicine_info(pr_id)
        ui.Selected_Medicine.clear()

        # Iterate over medicine_info and extract English names
        for medicine in medicine_info:
            english_name = medicine['English_Name']
            ui.Selected_Medicine.append(english_name)
        ui.Search()
        Favorite_Orientation.display_favorite_medicines(ui)

        # Prescription_Orientation.create_prescription_widget(self,medicine_info)
        Prescription_Orientation.Create_Prescription(ui)
        Prescription_Orientation.Add_To_Prescription_Page(ui)

        # Now Selected_Medicine contains English names from medicine_info
    @staticmethod
    def Load_History_Prescription(ui):
        # Create widget to hold the content
        content_widget = QWidget(ui.scrollArea_4)
        content_layout = QVBoxLayout(content_widget)

        # Load prescription details from database
        prescription_details = load_prescription_details()  # Replace with actual doctor ID

        # Sort prescription details in descending order based on prescription ID (prescription[0])
        prescription_details.sort(key=lambda x: x[0], reverse=True)

        # Add widgets created by create_history_widgets to the content layout
        for prescription in prescription_details:
            prescription_widget = History_Orientation.create_history_widgets(ui, prescription[0], prescription[1],
                                                                             prescription[2])
            content_layout.addWidget(prescription_widget)

        # Set the content widget for the scroll area
        ui.scrollArea_4.setWidget(content_widget)

    @staticmethod
    def Clear_History_Page(ui):
        # Get the scroll area's content widget
        scroll_content1 = ui.scrollArea_4.widget()

        # Clear existing layout and widgets
        if scroll_content1 is not None:
            # Remove the content widget from the scroll area
            ui.scrollArea_4.takeWidget()

            # Delete the content widget
            scroll_content1.deleteLater()








