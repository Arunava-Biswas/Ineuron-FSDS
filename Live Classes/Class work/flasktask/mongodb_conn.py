import pymongo


# create connection
def connect():
    try:
        client = pymongo.MongoClient("mongodb+srv://ineuron:Project1@cluster0.rp4qzrr.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print(e)
    else:
        # creating database and collection
        db = client["iNeuron"]
        coll = db["students"]
        return coll


# Inserting the data into the collection
def rec_insert(coll, record):
    try:
        coll.insert_one(record)
    except Exception as e:
        print(e)
    else:
        return "Data inserted successfully."


# finding all the records
def rec_find(coll):
    try:
        results = coll.find()
    except Exception as e:
        print(e)
    else:
        return results


# for update
def rec_upd(coll, present_data, new_data):
    try:
        coll.update_one(present_data, new_data)
    except Exception as e:
        print(e)
    else:
        return "Data updated successfully."


# for delete
def rec_del(coll, delete_query):
    try:
        coll.delete_one(delete_query)
    except Exception as e:
        print(e)
    else:
        return "Data deleted successfully."
