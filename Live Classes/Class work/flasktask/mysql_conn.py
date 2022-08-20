# Creating functions for MySQL

import mysql.connector as conn
from mysql.connector import Error
import logging as lg

logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%d/%m/%Y %I:%M:%S %p')
file_handler = lg.FileHandler('F:\\Pycharm_python\\Flaskapp\\Server_log\\mysql_logfile.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# Connecting to the database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = conn.connect(host=host_name, user=user_name, passwd=user_password, database=db_name)
        logger.info("Connection to mysql database is successful")

    except Error as err:
        logger.error(f"Error is: {err}")

    else:
        return connection


# Executing query
def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        logger.info("Query execution was successful")

    except Error as err:
        logger.error(f"Error is: {err}")

    else:
        return "Query execution was successful"


# Showing query results
def read_query(connection, query):
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info("Query reading was successful")

    except Error as err:
        logger.error(f"Error: {err}")

    else:
        return result
