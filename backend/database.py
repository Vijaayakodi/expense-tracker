import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT"))
        )

        print("✅ Connected to Railway MySQL")
        return connection

    except Exception as e:
        print("========== DATABASE ERROR ==========")
        print("HOST =", os.getenv("DB_HOST"))
        print("USER =", os.getenv("DB_USER"))
        print("DATABASE =", os.getenv("DB_NAME"))
        print("PORT =", os.getenv("DB_PORT"))
        print("ERROR =", repr(e))
        print("===================================")
        return None