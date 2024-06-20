import mysql.connector

import Authentication


# zakaria
# database="pharmacy_system",
# password="RootPass24@"
# behiry
#database = "smart_pharmacy",
#password = "Ahlynumber1#"
#sherief
# database="dumb_pharmacy",
# password="24920963King$"
db_connection_details = {
    "host": "127.0.1.1",
    "port": "3306",
    "user": "root",
    "database": "smart_pharmacy",
    "password": "Ahlynumber1#"
}

def search_medicine_data(keyword, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
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

def SearchStartUpMedicine(db_connection_details=db_connection_details):
    import string
    all_results = []
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
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
    return all_results

def get_medicine_id(english_name, active_substance, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()
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

def get_Pr_medicine_id(english_name, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT Medicine_ID FROM medicine_data WHERE English_Name = %s "
            cursor.execute(query, (english_name,))
            result = cursor.fetchone()
            if result:
                medicine_id = result[0]
                return medicine_id
            else:
                print("Medicine not found with the provided name")
                return None
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            connection.close()

def get_dr_id_from_email(email, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()
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

def add_to_favorite(dr_id, medicine_ids, db_connection_details=db_connection_details):
    if dr_id is None:
        print("Failed to add to favorites: Doctor ID not found.")
        return
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()
            select_query = "SELECT medicine_id FROM favorate_data WHERE dr_id = %s"
            cursor.execute(select_query, (dr_id,))
            existing_ids = {row[0] for row in cursor.fetchall()}
            insert_query = "INSERT INTO favorate_data (dr_id, medicine_id) VALUES (%s, %s)"
            values = [(int(dr_id), int(med_id)) for med_id in medicine_ids if med_id is not None and int(med_id) not in existing_ids]
            cursor.executemany(insert_query, values)
            connection.commit()
            print("Inserted into favorate_data table successfully")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def load_favorite_medicines(dr_id, db_connection_details=db_connection_details):
    favorite_medicines = []
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
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

def delete_from_favorite(dr_id, medicine_id, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()
            delete_query = "DELETE FROM favorate_data WHERE dr_id = %s AND medicine_id = %s"
            cursor.execute(delete_query, (dr_id, medicine_id))
            connection.commit()
            print("Deleted from favorite_data table successfully")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_medicine_info(medicine_name, db_connection_details=db_connection_details):
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT English_Name, Medicine_Price, Medicine_Usage FROM medicine_data WHERE english_name = %s"
            cursor.execute(select_query, (medicine_name,))
            medicine_info = cursor.fetchone()
            cursor.fetchall()
            print("Medicine info retrieved successfully")
            return medicine_info
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def add_prescription_data(patient_name, patient_age, dr_id, prescription_date, medicines,
                          db_connection_details=db_connection_details):
    prescription_id = None  # Initialize prescription_id variable

    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor()

            # Insert data into the prescription table
            insert_query = "INSERT INTO prescription (Patient_Name, Patient_Age, Dr_ID, Prescription_Date) VALUES (%s, %s, %s, %s)"
            data = (patient_name, patient_age, dr_id, prescription_date)
            cursor.execute(insert_query, data)
            connection.commit()
            prescription_id = cursor.lastrowid  # Get the last inserted ID

            # Insert data into the prescription_data table
            for medicine_id, count in medicines.items():
                insert_query = "INSERT INTO prescription_data (Prescription_ID, Medicine_ID, Medicine_Count) VALUES (%s, %s, %s)"
                data = (prescription_id, medicine_id, count)
                cursor.execute(insert_query, data)
            connection.commit()

            print("Inserted data into prescription table successfully")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return prescription_id  # Return the prescription ID

def load_prescription_details(db_connection_details=db_connection_details):
    prescription_details = []
    dr_id = get_dr_id_from_email(Authentication.mail)
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT Prescription_ID, Patient_Name, Prescription_Date FROM prescription WHERE Dr_ID = %s"
            cursor.execute(select_query,(dr_id,))
            prescription_records = cursor.fetchall()
            for record in prescription_records:
                prescription_details.append((record['Prescription_ID'], record['Patient_Name'], record['Prescription_Date']))
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
    return prescription_details


def search_prescription_by_id_or_name(search_term, db_connection_details=db_connection_details):
    prescription_details = []
    dr_id = get_dr_id_from_email(Authentication.mail)
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            # Search for records matching the search term in prescription table
            select_query = "SELECT Prescription_ID, Patient_Name, Prescription_Date FROM prescription WHERE Dr_ID = %s AND (Prescription_ID = %s OR Patient_Name LIKE %s)"
            cursor.execute(select_query, (dr_id, search_term, f"%{search_term}%"))
            prescription_records = cursor.fetchall()
            for record in prescription_records:
                prescription_details.append((record['Prescription_ID'], record['Patient_Name'], record['Prescription_Date']))
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
    return prescription_details


def retrieve_medicine_info(prescription_id, db_connection_details=db_connection_details):
    medicine_info = []
    try:
        connection = mysql.connector.connect(**db_connection_details)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Select medicine IDs and counts from prescription_data based on prescription ID
            select_prescription_query = "SELECT Medicine_ID, Medicine_Count FROM prescription_data WHERE Prescription_ID = %s"
            cursor.execute(select_prescription_query, (prescription_id,))
            prescription_records = cursor.fetchall()

            # Loop through prescription records to fetch medicine details
            for record in prescription_records:
                medicine_id = record['Medicine_ID']
                medicine_count = record['Medicine_Count']

                # Select medicine details from medicine_data based on medicine ID
                select_medicine_query = "SELECT English_Name, Medicine_Usage, Medicine_Price FROM medicine_data WHERE Medicine_ID = %s"
                cursor.execute(select_medicine_query, (medicine_id,))
                medicine_record = cursor.fetchone()

                # Add medicine details to medicine_info list
                if medicine_record:
                    medicine_info.append({
                        'Medicine_ID': medicine_id,
                        'English_Name': medicine_record['English_Name'],
                        'Usage': medicine_record['Medicine_Usage'],
                        'Price': medicine_record['Medicine_Price'],
                        'Count': medicine_count
                    })

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

    return medicine_info





