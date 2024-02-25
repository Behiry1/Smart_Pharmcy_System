from PySide6.QtCore import QTimer
import mysql.connector


def show_registration_error(ui, message):
    ui.ErrorMessage.setText(message)
    ui.ErrorMessage.setStyleSheet("color: red;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_registration_success(ui, message):
    ui.ErrorMessage.setText(message)
    ui.ErrorMessage.setStyleSheet("color: green;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_login_error(ui, message):
    ui.ErrorMessage_2.setText(message)
    ui.ErrorMessage_2.setStyleSheet("color: red;")
    QTimer.singleShot(5000, lambda: clear_errors(ui))
def show_login_success(ui, message):
    ui.ErrorMessage_2.setText(message)
    ui.ErrorMessage_2.setStyleSheet("color: green;")
    QTimer.singleShot(5000,lambda: clear_errors(ui))
def clear_errors(ui):
    ui.ErrorMessage.setText("")
    ui.ErrorMessage_2.setText("")
def doctor_register(ui, email, password, first_name, last_name, phone_number, department):
    table_name = "Doctor_Info"

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            #zakaria
            database="pharmacy_system",
            password="RootPass24@"
            #behiry
            # database="smart_pharmacy",
            # password="Ahlynumber1#"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor(prepared=True)
            check_query = "SELECT * FROM {} WHERE {}_Email = %s".format(table_name, "Dr")
            cursor.execute(check_query, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                # Insert doctor information using prepared statement
                insert_query = ("INSERT INTO Doctor_Info (Dr_FirstName, Dr_LastName, Dr_Email, Dr_Password, Dr_phoneNumber, Dr_Department) "
                                "VALUES (%s, %s, %s, %s, %s, %s)")
                insert_values = (first_name, last_name, email, password, int(phone_number), department)
                cursor.execute(insert_query, insert_values)
                connection.commit()

                show_registration_success(ui, "Registration successful.")
                return True

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_registration_error(ui, "Failed to connect to the database.")

    finally:
        if connection:
            connection.close()
            print("MySQL connection closed")

def pharmacist_register(ui, email, password, first_name, last_name, phone_number):
    table_name = "Pharmacist_Info"

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            #zakaria
            #database="pharmacy_system",
            #password="RootPass24@"
            #behiry
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor(prepared=True)  # Use prepared statements

            # Check for existing email (using prepared statement)
            check_query = "SELECT * FROM {} WHERE {}_Email = %s".format(table_name, "Pharm")
            cursor.execute(check_query, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                insert_query = ("INSERT INTO Pharmacist_Info (Pharm_FirstName, Pharm_LastName,Pharm_Email, Pharm_Password, Pharm_phoneNumber) "
                                "VALUES (%s, %s, %s, %s, %s)")
                insert_values = (first_name, last_name, email, password, int(phone_number))
                cursor.execute(insert_query, insert_values)
                connection.commit()


                show_registration_success(ui, "Registration successful.")
                return True



    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_registration_error(ui, "Failed to connect to the database.")

    finally:
        if connection:
            connection.close()
            print("MySQL connection closed")

def login_user(ui, email, password):
    succeeded_Fl = False
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            #zakaria
            #database="pharmacy_system",
            #password="RootPass24@"
            #behiry
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            # Create cursor
            cursor = connection.cursor()

            # Check login credentials in Doctor_Info table
            cursor.execute("SELECT * FROM Doctor_Info WHERE Dr_Email = %s AND Dr_Password = %s", (email, password))
            doctor_user = cursor.fetchone()

            # Check login credentials in Pharmacist_Info table
            cursor.execute("SELECT * FROM Pharmacist_Info WHERE Pharm_Email = %s AND Pharm_Password = %s",
                           (email, password))
            pharmacist_user = cursor.fetchone()

            if doctor_user or pharmacist_user:
                show_login_success(ui, "login successful.")
                #time.sleep(1)
                return True

            else:
                show_login_error(ui, "Invalid email or password. Please try again.")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_login_error(ui, "Failed to connect to the database.")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


import mysql.connector

def search_medicine_data(keyword):
    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            # zakaria
            # database="pharmacy_system",
            # password="RootPass24@"
            # behiry
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Execute the query to search for medicine based on the keyword
            query = "SELECT English_Name, Medicine_Price, Active_Substance FROM medicine_data WHERE English_Name LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))

            # Fetch all results
            results = cursor.fetchall()
            return results

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()