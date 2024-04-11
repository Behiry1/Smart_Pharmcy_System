from datetime import datetime

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QPdfWriter, QPageSize, QPainter, QPixmap, Qt


from Dr_MainWindow_Orientation import Favorite_Orientation,MainPages_Orientation,Prescription_Orientation,History_Orientation
from Dr_MainWindow_Database import get_medicine_id, get_dr_id_from_email, add_to_favorite, load_favorite_medicines, \
    SearchStartUpMedicine, search_medicine_data, get_Pr_medicine_id, add_prescription_data
import Authentication

class Favorite_Functions:
    @staticmethod
    def load_favorite_data(ui, favorite_medicines, favorite_state):
        print("Welcome")
        email = Authentication.mail
        drid = get_dr_id_from_email(email)
        favorite_meds = load_favorite_medicines(drid)

        if favorite_meds:
            favorite_medicines.extend(favorite_meds)

            for m in favorite_meds:
                english_name = m[0]
                active_substance = m[1]
                favorite_state[(english_name, active_substance)] = True

            Favorite_Orientation.display_favorite_medicines(ui)
        else:
            print("No favorite medicines found for this doctor ID.")

class MainPages_Functions:
    @staticmethod
    def StartUpMedicine(ui):
        all_results = SearchStartUpMedicine()


        email = Authentication.mail
        drid = get_dr_id_from_email(email)

        if all_results:
            # Fetch favorite medicines
            favorite_medicines = load_favorite_medicines(drid)
            # Dictionary to store favorite states for each medicine
            for result in all_results:
                english_name = result['English_Name']
                active_substance = result['Active_Substance']
                ui.favorite_state[(english_name, active_substance)] = False  # Initialize all to unfavorited

            # Check favorite medicines and set their button states
            if favorite_medicines:
                for result in all_results:
                    english_name = result['English_Name']
                    active_substance = result['Active_Substance']
                    if (english_name, active_substance) in favorite_medicines:
                        ui.favorite_state[(english_name, active_substance)] = True

            MainPages_Orientation.AddFrames(ui,all_results)
        else:
            print("No medicines found.")

class Prescription_Functions:

    @staticmethod

    @staticmethod
    def Print(ui):
        patient_name = ui.Patient_name_lineEdit.text().strip()
        patient_age = ui.Patient_name_lineEdit_2.text().strip()
        patient_age = int(patient_age)
        email = Authentication.mail
        drid = get_dr_id_from_email(email)
        Pr_date = ui.label_29.text().strip()
        medicines_dict = dict(Prescription_Orientation.get_medicine_counts(ui))
        Pr_Id = add_prescription_data(patient_name, patient_age, drid, Pr_date, medicines_dict)
        ui.label_32.setText(str(Pr_Id))
        original_stylesheet = ui.orderPage.styleSheet()

        # Define the directory where the PDFs will be saved
        save_directory = "D:/Project/Graduation_Project/Smart_Pharmcy_System/Application_Pharm/Pdfs/"

        # Create the filename using the patient's name
        pdf_filename = save_directory + patient_name + "_Prescription.pdf"

        # Create a PDF writer object
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
        ui.orderPage.resize(frame_width_pixels, frame_height_pixels)

        ui.Edite.hide()
        # self.pushButton_Trash.resize(0)
        ui.Print_Frame.hide()

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

        ui.orderPage.setStyleSheet(font_stylesheet)

        # Create a pixmap to render the OrderPage widget onto it
        pixmap = QPixmap(ui.orderPage.size())
        pixmap.fill(Qt.white)  # Fill pixmap with white background
        ui.orderPage.render(pixmap)

        # Draw the pixmap onto the PDF
        painter.drawPixmap(0, 0, pixmap)

        # Finish writing to the PDF file
        painter.end()

        # Open the PDF file using a PDF viewer
        QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_filename))

        ui.Edite.show()
        # self.pushButton_Trash.resize(0)
        ui.Print_Frame.show()
        ui.orderPage.setStyleSheet(original_stylesheet)
        Prescription_Orientation.Clear_Prescription_Page1(ui)
        History_Orientation.Load_History_Prescription(ui)
        ui.HomePage()

#class History_Functions:







