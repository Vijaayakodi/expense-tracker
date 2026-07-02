import mysql.connector
from mysql.connector import Error


def get_db_connection():
    """
    Creates and returns a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vijay232349k",
            database="expense_tracker"
        )

        if connection.is_connected():
            print("✅ Connected to MySQL")

        return connection

    except Error as e:
        print(f"❌ Database Error: {e}")
        return None