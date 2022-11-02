import base64
from datetime import datetime
import time
from bson import ObjectId
from pymongo import MongoClient
from gridfs import GridFS

# connect to MongoDB
client = MongoClient(
    "mongodb+srv://P000182:VSDXjUNidZfXlCwD@p000182-cluster.tg3lsmb.mongodb.net/?retryWrites=true&w=majority"
)

# get the database
db = client.get_database("p00082csitcp_blockchain")  # input your database name

# get the collection(=table)
users = db.User  # input youe collection name
files = db.File
messages = db.Message

# # count document(=row)
# print(users.count_documents({}))

# # count document(=row)
# print(users.count_documents({}))

# # mql for creating new document in User collection
# new_user = {
#     "username": "Yingying Guo",
#     "password": "abcabc"
# }

# # run the mql on User collection
# users.insert_one(new_user)

# # # find documents
# # print(list(users.find()))

# # find with the filter
# user = users.find_one({"username": "Yingying Guo", "password": "abcdefg"})
# print(user)
# print(type(user))

# # update documents
# # the filter
# user_update = {
#     "password": "abcdefg"
# }
# users.update_one({"username": "Yingying Guo"}, {"$set": user_update})

# # delete documents
# users.delete_one({"username": "alice"})


# timestamp = datetime.now()

# messages.update_one({"sender": "tom"}, {"$set": {"time": timestamp}})
def file_to_byte(file):
    with open(file, "rb") as fp:
        tu = base64.b64encode(fp.read())
    return tu


def byte_to_file(outfile, bin):
    #     image = Image.open(io.BytesIO(byte_data))
    #     return image

    tu_b = base64.b64decode(bin)
    with open(outfile, "wb") as fp:
        fp.write(tu_b)


file = "C:/Users/bagoo/Desktop/tet.txt"
# outfile = "C:/Users/bagoo/Desktop/test.txt"

# bin = file_to_byte(file)
# print(bin)
# byte_to_file(outfile, bin)
# new_file = {
#     "file_type": "image",
#     "file_name": "EPcover.jpg",
#     "file": bin

# }
# files.insert_one(new_file)

# photo = files.find_one({"_id": ObjectId("6360e2b36b655a6877c98f7e")})

# outfile = "C:/Users/bagoo/Desktop/" + photo["file_name"]
# bin = photo["file"]
# byte_to_file(outfile, bin)
