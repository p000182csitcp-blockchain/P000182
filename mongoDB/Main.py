from User import *
from MongoDatabase import *
import base64
from UserFactory import *
from bson.objectid import ObjectId

# test mongoDatabase.py #########################################################################################################################################
mDb = MongoDatabase()

# deployments = mDb.getDeployment()

# # storage a new record on mongoDB
# def new_record(file_name):

#     with open(file_name, 'rb') as fp:
#         record = base64.b64encode(fp.read())

#     # mql for creating new document in Deployment collection
#     new_deployment = {
#         "file_name": file_name,
#         "record": record
#     }

#     # run the mql on Deployment collection
#     deployments.insert_one(new_deployment)

# get record from mongoDB


# def get_record(file_name):
#     bin = deployments.find_one({"file_name": file_name})["record"]
#     record = base64.b64decode(bin)
#     with open(file_name, 'wb') as fp:
#         fp.write(record)


# # record's file name
# file_name = "0xfffC35fBeE13B4ef21ed001475d935a7B28E422f.json"
# # record's file directory
# file_path = "C:/Users/bagoo/Desktop/certificate_authority/build/deployments/5/" + \
#     filename
# new_record(filename)
# file_name = "0xfffC35fBeE13B4ef21ed001475d935a7B28E422f.json"
# file-path = "test.json"
# get_record(filename)

# test UserFactory.py #########################################################################################################################################
userFact = UserFactory()

# user = User("YYGzzzzzzzzzz", "123", "11", "bagoone@163.com", "0478639834")
# print(user.get_username())
# print(user.get_password())
# print(user.get_wallet_key())
# print(user.get_email())
# print(user.get_phone_number())
# user.set_keypairs(user.new_keyPairs(1024))
# print(user.get_keypairs().get_private_key())
# print(user.get_keypairs().get_public_key())
# print(user.get_message())
# print(user.get_private_key_location())
# print(user.get_photo())

# userFact.create_user("YYGzzzzzzzzzz", "123", "11",
#                      "bagoone@163.com", "0478639834", 1024)
# user_creat = userFact.get_user()
# print(user_creat.get_username())
# print(user_creat.get_password())
# print(user_creat.get_wallet_key())
# print(user_creat.get_email())
# print(user_creat.get_phone_number())
# print(user_creat.get_keypairs().get_private_key())
# print(user_creat.get_keypairs().get_public_key())
# print(user_creat.get_message())
# print(user_creat.get_private_key_location())
# print(user_creat.get_photo())

# user_check = userFact.check_user("YYGzzzzzzzzzz", "123")
# print(user_check.get_username())
# print(user_check.get_password())
# print(user_check.get_wallet_key())
# print(user_check.get_email())
# print(user_check.get_phone_number())
# print(user_check.get_keypairs().get_private_key())
# print(user_check.get_keypairs().get_public_key())
# print(user_check.get_message())
# print(user_check.get_private_key_location())
# print(user_check.get_photo())

# print(userFact.is_exist_username("Yingying"))

users = mDb.getUser()

# # mql for creating new document in User collection
# new_user = {
#     "username": "YY",
#     "password": "123",
#     "wallet_key": "11",
#     "email": "11",
#     "phone_number": "1111",
#     "photo": {
#         "_id": ObjectId("636233805fd4807aa0666384")
#     },
#     "private_key": "1111",
#     "public_key": "11111",
#     "private_key_location": "1111",
#     "message": {}
# }

# # run the mql on User collection
# users.insert_one(new_user)

# user_message = {
#     "message":
#     {
#         "_id": ObjectId("6357d0a14642d3887590c2aa"),
#     }
# }
# users.update_one({"username": "Yingying Guo"}, {
#     "$push": user_message})


# files = mDb.getFile()

# file = "MongoDB/DefaultPhoto.jpg"


# def file_to_byte(file):
#     with open(file, 'rb') as fp:
#         bin = base64.b64encode(fp.read())
#     return bin


# bin = userFact.file_to_byte(file)

# new_file = {
#     "user_id": ObjectId("635fcf690b01571902ccfaa3"),
#     "file_type": "image",
#     "file_name": "DefaultPhoto.jpg",
#     "file": bin
# }

# files.insert_one(new_file)


# user_log = User("YYGzzzzzzzzzzd", "123")

# pipeline = [
#     {
#         "$match": {
#             "username": user_log.get_username(),
#             "password": user_log.get_password()
#         }
#     },
#     {
#         "$lookup": {
#             "from": 'Message',
#             "localField": 'message.message_id',
#             "foreignField": '_id',
#             "as": 'message'
#         }
#     }
# ]

# user_record = users.aggregate(pipeline)

# count = 0

# for user_information in user_record:
#     user_check = User("", "", user_information["wallet_key"],
#                       user_information["email"], user_information["phone_number"])
#     count += 1

# if (count == 0):
#     print("usename or password is wrong")

# for user_information in user_record:

#     print(user_information["message"])


# userFact.update_photo("YYGzzzzzzzzzz", "file/EP.jpg")
# user_check = userFact.check_user("YYGzzzzzzzzzz", "123")

# message = Message("YYG", "YYGzzzzzzzzzz", "ENCRYPTED",
#                   "welcome to blockchain", "text")

# userFact.insert_message(message)