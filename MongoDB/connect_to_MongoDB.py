from pymongo import MongoClient
# connect to MongoDB
client = MongoClient("mongodb+srv://P000182:VSDXjUNidZfXlCwD@p000182-cluster.tg3lsmb.mongodb.net/?retryWrites=true&w=majority")

# get the database
db = client.get_database('p00082csitcp_blockchain')  # input your database name

# get the collection(=table)
users = db.User  # input youe collection name
files = db.File
messages = db.Message

# count document(=row)
print(users.count_documents({}))

# count document(=row)
print(users.count_documents({}))

# mql for creating new document in User collection
new_user = {
    "username": "Yingying Guo",
    "password": "abcabc"
}

# run the mql on User collection
users.insert_one(new_user)

# find documents
print(list(users.find()))

# find with the filter
print(users.find_one({"username": "Yingying Guo"}))

# update documents
# the filter
user_update = {
    "password": "abcdefg"
}
users.update_one({"username": "Yingying Guo"}, {"$set": user_update})

# delete documents
users.delete_one({"username": "alice"})