from asyncio.windows_events import NULL
import base64
from email import message
from msilib.schema import Binary, File
import os
from MongoDB.Message import *
from MongoDB.MongoDatabase import *
from MongoDB.User import *
from bson.objectid import ObjectId


class UserFactory:

    def __init__(self):
        self._users = MongoDatabase().getUser()
        self._files = MongoDatabase().getFile()
        self._messages = MongoDatabase().getMessage()
        self._user = None

    # get file by file id(y)
    def get_file_by_id(self, file_id):
        post = self._files.find_one({"_id": ObjectId(file_id)})
        self.byte_to_file(post["file"], post["file_name"])
        return post["file_name"]

    # get User at sign in(y)

    def check_user(self, username, password) -> User:
        try:
            user_log = User(username, password)

            pipeline = [
                {
                    "$match": {
                        "username": user_log.get_username(),
                        "password": user_log.get_password()
                    }
                },
                {
                    "$lookup": {
                        "from": 'Message',
                        "localField": 'message.message_id',
                        "foreignField": '_id',
                        "as": 'message'
                    }
                }
            ]

            user_record = self._users.aggregate(pipeline)

            count = 0

            for user_information in user_record:
                count += 1
                user_check = User(username, password, user_information["wallet_key"],
                                  user_information["email"], user_information["phone_number"])
                photo = "file/photo.jpg"
                self.byte_to_file(user_information["photo"], photo)
                user_check.set_photo(photo)
                user_check.set_message(user_information["message"])
                user_check.set_private_key_location(
                    user_information["private_key_location"])

                private_key = "file/private_key.pem"
                self.byte_to_file(user_information["private_key"], private_key)

                public_key = "file/public_key.pem"
                self.byte_to_file(user_information["public_key"], public_key)

                keypairs = KeyPairs(
                    {
                        "private_key": private_key,
                        "public_key": public_key
                    },
                    user_information["key_length"]
                )
                user_check.set_keypairs(keypairs)

                self._user = user_check
                return user_check
            if (count == 0):
                raise Exception("usename or password is wrong")
        except Exception as e:
            print(e.args)
            return None

    # create a new user and store in databse(y)
    def create_user(self, username, password, wallet_key, email, phone_number, key_length):
        try:

            self._user = User(username, password, wallet_key,
                              email, phone_number)

            self._user.set_keypairs(self._user.new_keyPairs(key_length))

            # mql for creating new document in User collection
            new_user = {
                "username": self._user.get_username(),
                "password": self._user.get_password(),
                "wallet_key": self._user.get_wallet_key(),
                "email": self._user.get_email(),
                "phone_number": self._user.get_phone_number(),
                "photo": self.file_to_byte(self._user.get_photo()),
                "key_length": key_length,
                "private_key": self.file_to_byte(self._user.get_keypairs().get_private_key()),
                "public_key": self.file_to_byte(self._user.get_keypairs().get_public_key()),
                "private_key_location": self._user.get_private_key_location(),
                "message": []
            }

            # run the mql on User collection
            self._users.insert_one(new_user)

            return self._user
        except Exception:
            print("There is something wrong!")
            return NULL

    # check if the username exist(y)
    def is_exist_username(self, username) -> bool:
        try:
            user_record = self._users.find_one({"username": username})
            if (user_record is not None):
                return True
            else:
                return False
        except Exception:
            return False

    # update the user's photo(y)
    def update_photo(self, username, photo) -> bool:
        try:
            # update documents
            user_update = {
                "photo": self.file_to_byte(photo)
            }
            self._users.update_one({"username": username}, {
                                   "$set": user_update})
            return True
        except Exception:
            return False

    # insert a new message(y)
    def insert_message(self, message):

        # mql for creating new document in Message collection
        new_message = {
            "sender": message.get_sender(),
            "receiver": message.get_receiver(),
            "message_type": message.get_message_type(),
            "message": message.get_message(),
            "timestamp": message.get_timestamp(),
            "delivery_type": message.get_delivery_type()
        }
        # run the mql on User collection
        self._messages.insert_one(new_message)

        post = self._messages.find_one(
            {"sender": message.get_sender(), "receiver": message.get_receiver(), "timestamp": message.get_timestamp()})
        message_id = str(post['_id'])
        # print(message_id)
        # message_id = post['_id']

        # update user(receiver) message
        user_message = {
            "message":
            {
                "message_id": ObjectId(message_id),
            }
        }
        self._users.update_one({"username": message.get_receiver()}, {
                               "$push": user_message})

        # if the message is a file
        if (message.get_message_type() == "file"):

            new_file = {
                "message_id": ObjectId(message_id),
                "file_type": message.get_message().split(".")[-1],
                "file_name": message.get_message(),
                "file": self.file_to_byte(message.get_message())
            }

            # insert a new file
            self._files.insert_one(new_file)

            # get the new file id
            file_post = self._files.find_one(
                {"message_id": ObjectId(message_id)})
            file_id = str(file_post['_id'])

            # update the message with file id
            self._messages.update_one({"_id": ObjectId(message_id)}, {
                "$set": {"message": ObjectId(file_id)}})

    # change file into binary(y)
    def file_to_byte(self, file):
        with open(file, 'rb') as fp:
            bin = base64.b64encode(fp.read())
            fp.close()
        return bin

    # change binary into file(y)
    def byte_to_file(self, bin, file):
        content = base64.b64decode(bin)
        with open(file, 'wb') as fp:
            fp.write(content)
            fp.close()

    def set_user(self, user):
        self._user = user

    def get_user(self):
        return self._user

    # clear the file
    def clear_file_content(self, file):
        with open(file, "a+", encoding="utf-8") as fp:
            fp.truncate(0)
