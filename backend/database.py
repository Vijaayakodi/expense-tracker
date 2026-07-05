import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db_connection():
    try:
        print("========== ENV ==========")
        print("HOST:", os.getenv("DB_HOST"))
        print("PORT:", os.getenv("DB_PORT"))
        print("USER:", os.getenv("DB_USER"))
        print("DATABASE:", os.getenv("DB_NAME"))
        print("=========================")

        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        print("✅ DATABASE CONNECTED")

        return connection

    except Exception as e:
        print("DATABASE FAILED")
        print(e)
        return None