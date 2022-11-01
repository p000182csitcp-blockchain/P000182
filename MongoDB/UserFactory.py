from asyncio.windows_events import NULL
from MongoDB.MongoDatabase import MongoDatabase
from MongoDB.User import User


class UserFactoy:

    def __init__(self) -> None:
        self._users = MongoDatabase().getUser()
        self._files = MongoDatabase().getFile()
        self._messages = MongoDatabase().getMessage()

    # get User at sign in
    def getUser(self, username, password):
        self._user = User(username, password)
        user_record = self._users.find_one(
            {"username": self._user.get_username, "password": self._user.get_password})
        self._user = User(username, password, user_record['wallet_key'],
                          user_record['email'], user_record['phone_number'], user_record['key_length'])
        if ('photo' in user_record):
            self._user.set_photo(user_record['photo'])

    # create a new user and store in databse
    def CreateUser(self, username, password, wallet_key, email, phone_number, key_length):
        try:
            self._user = User(username, password, wallet_key,
                              email, phone_number, key_length)
            # mql for creating new document in User collection
            new_user = {
                "username": self._user.get_username,
                "password": self._user.get_password,
                "wallet_key": self._user.get_wallet_key,
                "email": self._user.get_email,
                "phone_number": self._user.get_phone_number,
                "private_key_location": self._user.get_private_key_locatione
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
    def UpdatePhoto(self, username, photo) -> bool:
        try:
            # update documents
            user_update = {
                "photo": photo
            }
            users.update_one({"username": username}, {"$set": user_update})
            return True
        except Exception:
            return False

    # change file into byte
    def file_to_byte(file) -> bytes:
        return NULL

    # change file into byte
    def byte_to_file(file) -> bytes:
        return NULL