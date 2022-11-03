from typing import Collection
from gridfs import Database
from pymongo import MongoClient

# (y)
class MongoDatabase:

    def __init__(self):
        try:
            # connect to MongoDB
            self._client = MongoClient(
                "mongodb+srv://P000182:VSDXjUNidZfXlCwD@p000182-cluster.tg3lsmb.mongodb.net/?retryWrites=true&w=majority")
            # get the database
            # input your database name
            self._db = self._client.get_database('p00082csitcp_blockchain')
        except Exception:
            print("Unable to connect to the server.")

    def getconnection(self) -> Database:
        return self._db

    # get the collection User(=table)
    def getUser(self) -> Collection:
        return self._db.User  # input youe collection name

    # get the collection File(=table)
    def getFile(self) -> Collection:
        return self._db.File  # input youe collection name

    # get the collection Message(=table)
    def getMessage(self) -> Collection:
        return self._db.Message  # input youe collection name

    # get the collection Deployment(=table)
    def getDeployment(self) -> Collection:
        return self._db.Deployment  # input youe collection name
