import mysql.connector
import base64
import hashlib
from Utilities import *
from security import *



mail = ""


def login_user(ui, email, password):
    global mail  # Declare 'mail' as a global variable so it can be modified inside the function

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

            cursor.execute("SELECT Dr_Password, Dr_Salt FROM Doctor_Info WHERE Dr_Email = %s", (email,))
            doctor_data = cursor.fetchone()

            if doctor_data is None:
                cursor.execute("SELECT Pharm_Password, Pharm_Salt FROM Pharmacist_Info WHERE Pharm_Email = %s",
                               (email,))
                pharmacist_data = cursor.fetchone()

                if pharmacist_data is None:
                    show_login_error(ui, "Invalid email or password. Please try again.")
                    return False

                hashed_password, salt = pharmacist_data
            else:
                hashed_password, salt = doctor_data

            if salt is not None:
                decoded_salt = base64.b64decode(salt.encode('utf-8'))
            else:
                decoded_salt = b''

            combined_password = decoded_salt + secret_pepper_key.encode('utf-8') + password.encode('utf-8')
            entered_hashed_password = hashlib.sha256(combined_password).hexdigest()

            if hashed_password == entered_hashed_password:
                # Set the 'mail' variable to the email only if it is not already set
                if not mail:
                    mail = email
                show_login_success(ui, "Login successful.")
                print(mail)
                return True
            else:
                show_login_error(ui, "Invalid email or password. Please try again.")
                return False

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        show_login_error(ui, "Failed to connect to the database.")
        return False

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")


def doctor_register(ui, email, password, first_name, last_name, phone_number, department):
    table_name = "Doctor_Info"

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            #database="dumb_pharmacy",
            #password="24920963King$"
            # zakaria
            # database="pharmacy_system",
            # password="RootPass24@"
            # behiry
            database = "smart_pharmacy",
            password = "Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor(prepared=True)
            check_query = "SELECT * FROM {} WHERE {}_Email = %s".format(table_name, "Dr")
            cursor.execute(check_query, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                # Generate salt for hashing
                salt = secrets.token_bytes(16)
                # Hash the password before insertion
                hashed_password = hash_password(password, salt, secret_pepper_key)

                # Encode the salt using Base64 encoding
                encoded_salt = base64.b64encode(salt).decode('utf-8')

                insert_query = (
                    "INSERT INTO Doctor_Info (Dr_FirstName, Dr_LastName, Dr_Email, Dr_Password, Dr_Salt, Dr_phoneNumber, Dr_Department) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                insert_values = (
                    first_name, last_name, email, hashed_password, encoded_salt, int(phone_number), department)
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
            # database="dumb_pharmacy",
            # password="24920963King$"
            # zakaria
            # database="pharmacy_system",
            # password="RootPass24@"
            # behiry
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor(prepared=True)

            # Check for existing email (using prepared statement)
            check_query = "SELECT * FROM {} WHERE {}_Email = %s".format(table_name, "Pharm")
            cursor.execute(check_query, (email,))
            existing_user = cursor.fetchone()

            if existing_user:
                show_registration_error(ui, "Email already exists. Please use a different email.")
            else:
                # Generate salt for hashing
                salt = secrets.token_bytes(16)
                # Hash the password before insertion
                hashed_password = hash_password(password, salt, secret_pepper_key)

                # Encode the salt using Base64 encoding
                encoded_salt = base64.b64encode(salt).decode('utf-8')

                insert_query = ("INSERT INTO Pharmacist_Info (Pharm_FirstName, Pharm_LastName,Pharm_Email, Pharm_Password,Pharm_Salt, Pharm_phoneNumber) "
                                "VALUES (%s, %s, %s, %s, %s, %s)")
                insert_values = (first_name, last_name, email, hashed_password, encoded_salt ,int(phone_number))
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
