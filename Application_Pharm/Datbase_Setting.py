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
    QTimer.singleShot(5000, lambda: clear_errors(ui))

def clear_errors(ui):
    ui.ErrorMessage.setText("")
    ui.ErrorMessage_2.setText("")

def doctor_register(ui, email, password, first_name, last_name, phone_number, department):
    table_name = "Doctor_Info"
    table_d = "Dr"

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            cursor.execute("SELECT * FROM {} WHERE {}_Email = %s".format(table_name, table_d), (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                cursor.execute("SELECT COUNT(*) AS total_count FROM doctor_info;")
                reslut = cursor.fetchone()
                count = reslut[0]
                id =  int(count)+1
                cursor.execute(
                    "INSERT INTO {} ({}_ID,{}_FirstName, {}_LastName, {}_Email, {}_Password, {}_phoneNumber, {}_Department) VALUES (%s,%s,%s,%s, %s, %s, %s, %s)".format(
                        table_name, table_d ,table_d, table_d, table_d, table_d,table_d,table_d),
                    (id,first_name, last_name, email, password, phone_number, department))
                connection.commit()
                show_registration_success(ui, "Registration successful.")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_registration_error(ui, "Failed to connect to the database.")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

def pharmacist_register(ui, email, password, first_name, last_name, phone_number):
    table_name = "Pharmacist_Info"
    table_d = "Pharm"

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )
        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            cursor.execute("SELECT * FROM {} WHERE {}_Email = %s".format(table_name, table_d), (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                cursor.execute("SELECT COUNT(*) FROM pharmacist_info;")
                count = cursor.fetchone()[0]
                id = count + 1
                insert_query = "INSERT INTO {} ({}_ID, {}_FirstName, {}_LastName, {}_Email, {}_Password, {}_phoneNumber) VALUES (NULL, %s, %s, %s, %s, %s, %s)".format(
                    table_name, table_d, table_d, table_d, table_d, table_d, table_d)
                insert_values = (first_name, last_name, email, password, phone_number)
                cursor.execute(insert_query, insert_values)
                connection.commit()
                show_registration_success(ui, "Registration successful.")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_registration_error(ui, "Failed to connect to the database.")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


def login_user(ui, email, password):
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
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
                show_login_success(ui, "Login successful.")
            else:
                show_login_error(ui, "Invalid email or password. Please try again.")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_login_error(ui, "Failed to connect to the database.")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")
