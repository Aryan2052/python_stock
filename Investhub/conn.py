import mysql.connector
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aryan2005",
        database="sma"
    )
    print("connected", db)

    # Create a cursor object
    cursor = db.cursor()
except mysql.connector.Error as e:
    print(f"Error {e}")
