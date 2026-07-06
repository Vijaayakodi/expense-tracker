import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_db_connection():
    print("\n========== ENV ==========")
    print("HOST:", repr(os.getenv("DB_HOST")))
    print("PORT:", repr(os.getenv("DB_PORT")))
    print("USER:", repr(os.getenv("DB_USER")))
    print("DATABASE:", repr(os.getenv("DB_NAME")))
    print("PASSWORD LENGTH:", len(os.getenv("DB_PASSWORD") or ""))
    print("=========================")

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            connection_timeout=10
        )

        print("✅ DATABASE CONNECTED")
        return connection

    except Exception as e:
        print("❌ DATABASE FAILED")
        print(type(e).__name__)
        print(e)
        return None