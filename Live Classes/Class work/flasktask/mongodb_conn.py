import pymongo
import logging as lg

logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)
formatter = lg.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%d/%m/%Y %I:%M:%S %p')
file_handler = lg.FileHandler('F:\\Pycharm_python\\Flaskapp\\Server_log\\mongodb_logfile.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# create connection
def connect():
    try:
        client = pymongo.MongoClient("mongodb+srv://ineuron:Project1@cluster0.rp4qzrr.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        logger.error(e)
    else:
        # creating database and collection
        db = client["iNeuron"]
        coll = db["students"]
        logger.info("Connection to mongodb is successful")
        logger.info("database and collection is created")
        return coll


# Inserting the data into the collection
def rec_insert(coll, record):
    try:
        coll.insert_one(record)
        logger.info("Data inserted successfully.")
    except Exception as e:
        logger.error(e)
    else:
        return "Data inserted successfully."


# finding all the records
def rec_find(coll):
    try:
        results = coll.find()
    except Exception as e:
        logger.error(e)
    else:
        logger.info("Record fetched successfully")
        return results


# for update
def rec_upd(coll, present_data, new_data):
    try:
        coll.update_one(present_data, new_data)
        logger.info("Data updated successfully.")
    except Exception as e:
        logger.error(e)
    else:
        return "Data updated successfully."


# for delete
def rec_del(coll, delete_query):
    try:
        coll.delete_one(delete_query)
        logger.info("Data deleted successfully.")
    except Exception as e:
        logger.error(e)
    else:
        return "Data deleted successfully."
