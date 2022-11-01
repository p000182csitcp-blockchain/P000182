from typing import Collection
from gridfs import Database
from pymongo import MongoClient


class MongoDatabase:
    # connect to MongoDB
    client = MongoClient(
        "mongodb+srv://P000182:VSDXjUNidZfXlCwD@p000182-cluster.tg3lsmb.mongodb.net/?retryWrites=true&w=majority")

    # get the database
    # input your database name
    db = client.get_database('p00082csitcp_blockchain')

    def getconnection(self) -> Database:
        return db

    # get the collection User(=table)
    def getUser(self) -> Collection:
        return db.User  # input youe collection name

    # get the collection File(=table)
    def getUser(self) -> Collection:
        return db.File  # input youe collection name

    # get the collection Message(=table)
    def getUser(self) -> Collection:
        return db.Message  # input youe collection name
