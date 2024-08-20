import mysql.connector

from db.db_main import DB_NAME


def get_connection():
    mysql.connector.connect(
        host='localhost',
        user='admin',
        password='admin',
        database=DB_NAME
    )
