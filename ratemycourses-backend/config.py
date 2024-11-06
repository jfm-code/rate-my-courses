import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DBHOST"),
    "dbname": os.getenv("DBNAME"),
    "user": os.getenv("DBUSER"),
    "password": os.getenv("DBPASSWORD"),
    "port": os.getenv("DBPORT")
}
