import mysql.connector
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


def get_prescription_details(prescription_id):

        # Create a connection to the database
        conn = mysql.connector.connect(
            host=db_connection_details["host"],
            port=db_connection_details["port"],
            user=db_connection_details["user"],
            password=db_connection_details["password"],
            database=db_connection_details["database"]
        )

        cursor = conn.cursor()

        # SQL query with location_x and location_y included
        query = """
        SELECT 
            m.English_Name AS Medicine_Name,
            m.Medicine_Usage,
            pd.Medicine_Count,
            m.Medicine_Price,
            CONCAT(d.Dr_FirstName, ' ', d.Dr_LastName) AS Dr_Name,
            p.Prescription_Date,
            p.flag,
            m.location_x,  # Add location_x
            m.location_y   # Add location_y
        FROM 
            prescription p
        JOIN 
            prescription_data pd ON p.Prescription_ID = pd.Prescription_ID
        JOIN 
            medicine_data m ON pd.Medicine_ID = m.Medicine_ID
        JOIN 
            doctor_info d ON p.Dr_ID = d.Dr_ID
        WHERE 
            p.Prescription_ID = %s
        """

        cursor.execute(query, (prescription_id,))
        results = cursor.fetchall()

        # Process results
        medicines = []
        dr_name = ""
        prescription_date = ""
        flag = ""

        for row in results:
            medicines.append({
                "Medicine_Name": row[0],
                "Medicine_Usage": row[1],
                "Medicine_Count": row[2],
                "Medicine_Price": row[3],
                "loc_x": row[7],  # Add location_x
                "loc_y": row[8]   # Add location_y
            })
            dr_name = row[4]
            prescription_date = row[5]
            flag = row[6]

        cursor.close()
        conn.close()
        print(medicines)


        return medicines, dr_name, prescription_date, flag



def insert_receipt_and_details(receipt_info, receipt_data):
    conn = mysql.connector.connect(
        host=db_connection_details["host"],
        port=db_connection_details["port"],
        user=db_connection_details["user"],
        password=db_connection_details["password"],
        database=db_connection_details["database"]
    )

    cursor = conn.cursor()

    # SQL query to insert into receipt table
    insert_receipt_query = """
    INSERT INTO receipt (Prescription_ID, Pharm_ID, Receipt_Date, Total_Price)
    VALUES (%s, %s, %s, %s)
    """

    # SQL query to insert into receipt_data table
    insert_receipt_data_query = """
    INSERT INTO receipt_data (Receipt_ID, Medicine_ID, Number_Of_Units, Price)
    VALUES (%s, %s, %s, %s)
    """

    # SQL query to update the flag in the prescription table
    update_prescription_flag_query = """
    UPDATE prescription SET flag = 1 WHERE Prescription_ID = %s
    """

    try:
        # Inserting data into receipt table
        cursor.executemany(insert_receipt_query, receipt_info)
        conn.commit()

        # Getting last inserted receipt ID
        last_receipt_id = cursor.lastrowid

        # Inserting data into receipt_data table
        for data in receipt_data:
            # Retrieve medicine_id based on medicine_name
            cursor.execute("SELECT Medicine_ID FROM medicine_data WHERE English_Name = %s", (data[0],))
            medicine_id = cursor.fetchone()[0]  # Assuming English_Name is unique

            # Inserting data into receipt_data table
            cursor.execute(insert_receipt_data_query, (last_receipt_id, medicine_id) + data[1:])
        conn.commit()

        # Update flag in prescription table
        for receipt_info_entry in receipt_info:
            cursor.execute(update_prescription_flag_query, (receipt_info_entry[0],))  # Assuming Prescription_ID is the first element in receipt_info
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()


def get_receipt_details(search_text=None):
    # Create a connection to the database
    conn = mysql.connector.connect(
        host=db_connection_details["host"],
        port=db_connection_details["port"],
        user=db_connection_details["user"],
        password=db_connection_details["password"],
        database=db_connection_details["database"]
    )

    cursor = conn.cursor()

    # SQL query to fetch prescription details from the receipt table
    if search_text:
        # Check if the search text can be converted to an integer (for Prescription_ID search)
        try:
            prescription_id = int(search_text)
            query = """
            SELECT 
                r.Prescription_ID,
                CONCAT(d.Dr_FirstName, ' ', d.Dr_LastName) AS Dr_Name,
                r.Receipt_Date,
                r.Total_Price
            FROM 
                receipt r
            JOIN 
                prescription p ON r.Prescription_ID = p.Prescription_ID
            JOIN 
                doctor_info d ON p.Dr_ID = d.Dr_ID
            WHERE 
                d.Dr_FirstName LIKE %s OR d.Dr_LastName LIKE %s OR r.Receipt_Date LIKE %s OR r.Prescription_ID = %s
            """
            search_pattern = f"%{search_text}%"
            cursor.execute(query, (search_pattern, search_pattern, search_pattern, prescription_id))
        except ValueError:
            query = """
            SELECT 
                r.Prescription_ID,
                CONCAT(d.Dr_FirstName, ' ', d.Dr_LastName) AS Dr_Name,
                r.Receipt_Date,
                r.Total_Price
            FROM 
                receipt r
            JOIN 
                prescription p ON r.Prescription_ID = p.Prescription_ID
            JOIN 
                doctor_info d ON p.Dr_ID = d.Dr_ID
            WHERE 
                d.Dr_FirstName LIKE %s OR d.Dr_LastName LIKE %s OR r.Receipt_Date LIKE %s
            """
            search_pattern = f"%{search_text}%"
            cursor.execute(query, (search_pattern, search_pattern, search_pattern))
    else:
        query = """
        SELECT 
            r.Prescription_ID,
            CONCAT(d.Dr_FirstName, ' ', d.Dr_LastName) AS Dr_Name,
            r.Receipt_Date,
            r.Total_Price
        FROM 
            receipt r
        JOIN 
            prescription p ON r.Prescription_ID = p.Prescription_ID
        JOIN 
            doctor_info d ON p.Dr_ID = d.Dr_ID
        """
        cursor.execute(query)

    results = cursor.fetchall()

    # Process results
    receipt_details = []

    for row in results:
        receipt_details.append({
            "Prescription_ID": row[0],
            "Dr_Name": row[1],  # Concatenated first name and last name
            "Date": row[2],
            "Total_Price": row[3]
        })

    cursor.close()
    conn.close()

    return receipt_details

def get_receipt_details_info(prescription_id):
    # Create a connection to the database
    conn = mysql.connector.connect(
        host=db_connection_details["host"],
        port=db_connection_details["port"],
        user=db_connection_details["user"],
        password=db_connection_details["password"],
        database=db_connection_details["database"]
    )

    cursor = conn.cursor()

    # SQL query to retrieve doctor's name, receipt date, and total price
    query1 = """
    SELECT 
        CONCAT(d.Dr_FirstName, ' ', d.Dr_LastName) AS Dr_Name,
        r.Receipt_Date,
        r.Total_Price
    FROM 
        prescription p
    JOIN 
        receipt r ON p.Prescription_ID = r.Prescription_ID
    JOIN 
        doctor_info d ON p.Dr_ID = d.Dr_ID
    WHERE 
        p.Prescription_ID = %s
    """

    cursor.execute(query1, (prescription_id,))
    result1 = cursor.fetchone()

    if not result1:
        print(f"No data found for Prescription ID: {prescription_id}")
        return [], []

    # Extract details from the first query
    dr_name = result1[0]
    receipt_date = result1[1]
    total_price = result1[2]

    # SQL query to retrieve medicine details with Number_Of_Units
    query2 = """
    SELECT 
        m.English_Name AS Medicine_Name,
        rd.Number_Of_Units,
        m.Medicine_Usage,
        rd.Price
    FROM 
        receipt r
    JOIN 
        receipt_data rd ON r.Receipt_ID = rd.Receipt_ID
    JOIN 
        medicine_data m ON rd.Medicine_ID = m.Medicine_ID
    WHERE 
        r.Prescription_ID = %s
    """

    cursor.execute(query2, (prescription_id,))
    result2 = cursor.fetchall()

    # Process results for medicine details
    medicine_details = []

    for row in result2:
        medicine_details.append({
            "Medicine_Name": row[0],
            "Medicine_Usage": row[2],
            "Number_of_units": row[1],
            "Price": row[3]
        })

    cursor.close()
    conn.close()

    # Return the doctor and receipt details as a dictionary, and medicine details as a list of tuples
    doctor_receipt_details = {
        "Doctor_Name": dr_name,
        "Receipt_Date": receipt_date,
        "Total_Price": total_price
    }

    return doctor_receipt_details, medicine_details

def get_specific_medicines_details():
    """
    Retrieve details (English name, active substance, price) of medicines
    whose English names contain predefined medicine names.

    :return: List of dictionaries containing medicine details for each requested medicine.
             Each dictionary contains keys: 'English_Name', 'Active_Substance', 'Price'.
    """
    # List of specific medicine names to search for
    medicine_names = ["panadol", "limitless", "adol", "zyrtec", "vitamax"]

    conn = mysql.connector.connect(
        host=db_connection_details["host"],
        port=db_connection_details["port"],
        user=db_connection_details["user"],
        password=db_connection_details["password"],
        database=db_connection_details["database"]
    )

    cursor = conn.cursor()

    # Prepare a list to store the results
    medicines_details = []

    try:
        # SQL query to retrieve details for specific medicines containing any of the names
        query = """
        SELECT English_Name, Active_Substance, Medicine_Price
        FROM medicine_data
        WHERE English_Name LIKE %s
        """

        # Execute the query for each medicine name
        for name in medicine_names:
            cursor.execute(query, ('%' + name + '%',))
            results = cursor.fetchall()

            for row in results:
                medicine_details = {
                    "English_Name": row[0],
                    "Active_Substance": row[1],
                    "Price": float(row[2])  # Assuming price is retrieved as a float
                }
                medicines_details.append(medicine_details)

    except mysql.connector.Error as e:
        print(f"Error retrieving medicine details: {e}")

    finally:
        cursor.close()
        conn.close()

    return medicines_details




