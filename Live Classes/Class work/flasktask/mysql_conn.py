# Creating functions for MySQL

import mysql.connector as conn
from mysql.connector import Error


# Connecting to the database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = conn.connect(host=host_name, user=user_name, passwd=user_password, database=db_name)

    except Error as err:
        print(f"Error is: {err}")

    else:
        return connection


# Executing query
def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()

    except Error as err:
        print(f"Error is: {err}")

    else:
        return "Query execution was successful"


# Showing query results
def read_query(connection, query):
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print("Query reading was successful")

    except Error as err:
        print(f"Error: {err}")

    else:
        return result
