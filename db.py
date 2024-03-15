import mysql.connector


def get_db_connection(username):
    database = username


    try:
        myDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=database
        )
        return myDB
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None


def get_init_db_connection():
    database = "smart_cafe_admin"


    try:
        myinitDB = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=database
        )
        return myinitDB
    except mysql.connector.Error as err:
        print("Database connection error:", err)
        return None
