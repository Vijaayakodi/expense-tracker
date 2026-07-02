from database import get_db_connection

connection = get_db_connection()

if connection:
    print("Database connection successful!")

    connection.close()
    print("Connection closed.")