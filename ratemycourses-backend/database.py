import psycopg2
from config import DB_CONFIG

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn
