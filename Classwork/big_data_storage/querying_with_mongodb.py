from pymongo import MongoClient
from datetime import datetime


client = MongoClient()


def create_mongodb():
    """
    NOTE: RUN THIS ONCE, IT CREATES A DATABASE
    """

    db = client['tutorial']
    coll = db['articles']

    doc = {
        "title": "An article about MongoDB and Python",
        "author": "Marco",
        "publication_date": datetime.utcnow(),
        # more fields
    }

    doc_id = coll.insert_one(doc).inserted_id


# create_mongodb()

# client = MongoClient()

def query_from_db():
    db = client['tutorial']
    coll = db['articles']

    for doc in coll.find():
        print(doc)

query_from_db()