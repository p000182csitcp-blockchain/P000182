from asyncio.windows_events import NULL
import base64
from email import message
from msilib.schema import Binary, File
from MongoDB.Message import Message
from MongoDB.MongoDatabase import MongoDatabase
from MongoDB.User import User
from bson.objectid import ObjectId


class UserFactoy:
    def __init__(self) -> None:
        self._users = MongoDatabase().getUser()
        self._files = MongoDatabase().getFile()
        self._messages = MongoDatabase().getMessage()

    # get User at sign in
    def getUser(self, username, password):
        self._user = User(username, password)
        user_record = self._users.find_one(
            {"username": self._user.get_username, "password": self._user.get_password}
        )
        self._user = User(
            username,
            password,
            user_record["wallet_key"],
            user_record["email"],
            user_record["phone_number"],
            user_record["key_length"],
        )
        if "photo" in user_record:
            self._user.set_photo(user_record["photo"])

    # create a new user and store in databse
    def createUser(
        self, username, password, wallet_key, email, phone_number, key_length
    ):
        try:
            self._user = User(
                username, password, wallet_key, email, phone_number, key_length
            )
            # mql for creating new document in User collection
            new_user = {
                "username": self._user.get_username,
                "password": self._user.get_password,
                "wallet_key": self._user.get_wallet_key,
                "email": self._user.get_email,
                "phone_number": self._user.get_phone_number,
                "private_key_location": self._user.get_private_key_locatione,
            }

            # run the mql on User collection
            self._users.insert_one(new_user)

            return self._user
        except Exception:
            return NULL

    # check if the username exist
    def isExistUsername(self, username) -> bool:
        try:
            user_record = self._users.find_one({"username": username})
            return True
        except Exception:
            return False

    # update the user's photo
    def updatePhoto(self, username, photo) -> bool:
        try:
            # update documents
            user_update = {"photo": photo}
            self._users.update_one({"username": username}, {"$set": user_update})
            return True
        except Exception:
            return False

    # insert a new message
    def insertMessage(self, message):

        # mql for creating new document in Message collection
        new_message = {
            "sender": message.get_sender,
            "receiver": message.get_receiver,
            "message_type": message.get_message_type,
            "message": message.get_message,
            "timestamp": message.get_timestamp,
            "transport_type": message.get_transport_type,
        }
        # run the mql on User collection
        self._messages.insert_one(new_message)

        post = self._messages.find_one(
            {
                "sender": message.get_sender,
                "receiver": message.get_receiver,
                "timestamp": message.get_timestamp,
            }
        )
        message_id = str(post["_id"])

        # update user(receiver) message
        user_message = {
            "message": {
                "_id": ObjectId(message_id),
            }
        }
        self._users.update_one(
            {"username": message.get_receiver}, {"$push": user_message}
        )

    # change image into binary
    def file_to_byte(file) -> Binary:
        with open(file, "rb") as fp:
            bin = base64.b64encode(fp.read())
        return bin

    # change binary into image
    def byte_to_file(bin, file):
        image = base64.b64decode(bin)
        with open(file, "wb") as fp:
            fp.write(image)
