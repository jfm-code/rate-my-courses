import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DBHOST"),
            port=os.getenv("DBPORT"),
            dbname=os.getenv("DBNAME"),
            user=os.getenv("DBUSER"),
            password=os.getenv("DBPASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise
