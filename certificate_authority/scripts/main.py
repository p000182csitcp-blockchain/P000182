from deployment.Record import Record
from MongoDB.UserFactory import UserFactory
from MongoDB.Message import Message
from MongoDB.MongoDatabase import *
from datetime import datetime
from scripts.cleanFile import *


def main():
    # create a user factory
    userFact = UserFactory()

    # # clean the file directory at start
    # # !!!add to start
    # clean_file()

    # # update records in mongoDB at sign up
    # # !!!add to login
    # Record().update_records()

    # # delete a file
    # # !!!add somewhere
    # userFact.delete_file("file/public_key.pem")

    # check user at sign in
    username = "t1"
    password = "123"
    # user = userFact.check_user(username, password)
    user = userFact.check_user_by_username("bob")
    if user is None:
        print("please input again")
    else:
        print(user.get_username())
        print(user.get_password())
        print(user.get_wallet_key())
        print(user.get_email())
        print(user.get_phone_number())
        print(user.get_keypairs().get_private_key())
        # print(user.get_keypairs().get_public_key())
        i = 0
        for mes in user.get_message():
            print(
                " ============================= message {} ==========================================".format(
                    i
                )
            )
            print("_id:" + str(mes["_id"]))
            print("sender:" + mes["sender"])
            print("receiver:" + mes["receiver"])
            print("message_type" + mes["message_type"])
            if mes["message_type"] == "file":
                file = userFact.get_file_by_id(mes["message"])
                print("message(file):" + file)
            else:
                print("message:" + mes["message"])
            print("timestamp:" + mes["timestamp"].strftime("%m/%d/%Y, %H:%M:%S"))
            print("delivery_type:" + mes["delivery_type"])
            i += 1
        print(user.get_private_key_location())
        print(user.get_photo())

    # # insert a new message
    # # !!!add to send_message and send_file
    # file = "file/DefaultPhoto.jpg"
    # message = Message("YYG", "YYGzzzzzzzzzz", "file",
    #                   file, "SIGNED")
    # if (message.get_delivery_type() == "SIGNED" or message.get_delivery_type() == "ENCRYPTED_AND_SIGNED"):
    #     message.set_signature("11111111111test test test")
    # userFact.insert_message(message)
