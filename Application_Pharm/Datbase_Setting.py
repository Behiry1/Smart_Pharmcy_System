from PySide6.QtCore import QTimer
import mysql.connector
from SignUp_Login import *
from security import *

from Utilities import *





def search_medicine_data(keyword):
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
            cursor = connection.cursor(dictionary=True)


            query = "SELECT English_Name, Medicine_Price, Active_Substance FROM medicine_data WHERE English_Name LIKE %s"
            cursor.execute(query, (f"%{keyword}%",))


            results = cursor.fetchall()
            return results

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def SearchStartUpMedicine():
    import string

    all_results = []

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

            cursor = connection.cursor(dictionary=True)

            for char in string.ascii_lowercase:

                query = "SELECT English_Name, Medicine_Price, Active_Substance FROM medicine_data WHERE English_Name LIKE %s LIMIT 10"
                cursor.execute(query, (char + '%',))


                results = cursor.fetchall()
                all_results.extend(results)

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

    return all_results

def get_medicine_id(english_name, active_substance):
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

            cursor = connection.cursor()

            # Query to retrieve medicine ID based on name and active substance
            query = "SELECT Medicine_ID FROM medicine_data WHERE English_Name = %s AND Active_Substance = %s"
            cursor.execute(query, (english_name, active_substance))
            result = cursor.fetchone()

            if result:
                medicine_id = result[0]
                return medicine_id
            else:
                print("Medicine not found with the provided name and active substance")
                return None

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

def get_dr_id_from_email(email):

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

            cursor = connection.cursor()

            # Query to retrieve dr_id based on email
            query = "SELECT dr_id FROM doctor_info WHERE dr_email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if result:
                dr_id = result[0]
                return dr_id
            else:
                print("Doctor not found with the provided email")
                return None

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

def add_to_favorite(dr_id, medicine_ids):
    if dr_id is None:
        print("Failed to add to favorites: Doctor ID not found.")
        return

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

            # Retrieve existing favorite medicine IDs for the doctor
            select_query = "SELECT medicine_id FROM favorate_data WHERE dr_id = %s"
            cursor.execute(select_query, (dr_id,))
            existing_ids = {row[0] for row in cursor.fetchall()}

            # Use executemany for batch insertion
            insert_query = "INSERT INTO favorate_data (dr_id, medicine_id) VALUES (%s, %s)"
            values = [(int(dr_id), int(med_id)) for med_id in medicine_ids if med_id is not None and int(med_id) not in existing_ids]
            cursor.executemany(insert_query, values)

            # Commit the transaction
            connection.commit()

            print("Inserted into favorate_data table successfully")

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

import mysql.connector

def load_favorite_medicines(dr_id):
    favorite_medicines = []

    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Query to retrieve favorite medicines for the given doctor ID
            select_query = "SELECT m.English_Name, m.Active_Substance " \
                           "FROM favorate_data AS f " \
                           "INNER JOIN medicine_data AS m ON f.medicine_id = m.Medicine_ID " \
                           "WHERE f.dr_id = %s"
            cursor.execute(select_query, (dr_id,))
            favorite_medicines_data = cursor.fetchall()

            for medicine_data in favorite_medicines_data:
                favorite_medicines.append((medicine_data['English_Name'], medicine_data['Active_Substance']))

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return favorite_medicines
def delete_from_favorite(dr_id, medicine_id):
    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Delete the favorite entry for the given doctor and medicine ID
            delete_query = "DELETE FROM favorate_data WHERE dr_id = %s AND medicine_id = %s"
            cursor.execute(delete_query, (dr_id, medicine_id))

            # Commit the transaction
            connection.commit()

            print("Deleted from favorite_data table successfully")

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

import mysql.connector

def get_medicine_info(medicine_name):
    try:
        connection = mysql.connector.connect(
            host="127.0.1.1",
            port="3306",
            user="root",
            database="smart_pharmacy",
            password="Ahlynumber1#"
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Select the medicine usage and price based on the medicine name
            select_query = "SELECT English_Name, Medicine_Price, Medicine_Usage FROM medicine_data WHERE english_name = %s"
            cursor.execute(select_query, (medicine_name,))
            medicine_info = cursor.fetchone()

            # Consume all remaining rows to prevent "Unread result found" error
            cursor.fetchall()

            print("Medicine info retrieved successfully")

            return medicine_info

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

