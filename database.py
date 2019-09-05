import pymongo


class DB(objects):
    """
    The class adds two basic functions - insert and find_one 
    to search and insert documents in our collection.
    """

    URI = "mongodb://127.0.0.1:27017"

    @staticmethod 
    async def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['blog']

    @staticmethod 
    async def insert(collection, data):
        return DB.DATABASE[collection].insert(data)

    @staticmethod
    async def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)