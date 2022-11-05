from deployment.Record import Record
from MongoDB.UserFactory import UserFactory
from MongoDB.Message import Message
from MongoDB.MongoDatabase import *
from datetime import datetime


def main():
    # # insert records
    # filename = "build/deployments/5/"
    # Record().new_record(filename)

    # record download
    Record().get_record()

    # create a user factory
    userFact = UserFactory()

    # # create a user at sign up
    # username = ""
    # password = ""
    # wallet_key = ""
    # email = ""
    # phone_number = ""
    # key_length = 1024
    # if (userFact.is_exist_username(username)):
    #     print("The username already exist. Please change one.")
    # else:
    #     userFact.create_user(username, password, wallet_key,
    #                          email, phone_number, key_length)

    # # check user at sign in
    # username = "YYGzzzzzzzzzz"
    # password = "123"
    # user = userFact.check_user(username, password)
    # if (user is None):
    #     print("please input again")
    # else:
    #     print(user.get_username())
    #     print(user.get_password())
    #     print(user.get_wallet_key())
    #     print(user.get_email())
    #     print(user.get_phone_number())
    #     print(user.get_keypairs().get_private_key())
    #     print(user.get_keypairs().get_public_key())
    #     i = 0
    #     for mes in user.get_message():
    #         print(
    #             " ============================= message {} ==========================================".format(i))
    #         print("_id:" + str(mes["_id"]))
    #         print("sender:" + mes["sender"])
    #         print("receiver:" + mes["receiver"])
    #         print("message_type" + mes["message_type"])
    #         if (mes["message_type"] == "file"):
    #             file = userFact.get_file_by_id(mes["message"])
    #             print("message(file):" + file)
    #         else:
    #             print("message:" + mes["message"])
    #         print("timestamp:" +
    #               mes["timestamp"].strftime("%m/%d/%Y, %H:%M:%S"))
    #         print("delivery_type:" + mes["delivery_type"])
    #         i += 1
    #     print(user.get_private_key_location())
    #     print(user.get_photo())

    # # create a new message
    # file = "file/DefaultPhoto.jpg"

    # message = Message("YYG", "YYGzzzzzzzzzz", "file",
    #                   file, "SIGNED")

    # userFact.insert_message(message)

    # get the collection(=table)
    users = MongoDatabase().getUser()  # input youe collection name

    # find documents
    print(userFact.get_all_username())
