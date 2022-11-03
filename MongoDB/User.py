import hashlib
import string
from Crypto.PublicKey import RSA
from MongoDB.KeyPairs import KeyPairs
from MongoDB.Message import Message


class User:

    def encodeByHash(self, str) -> string:
        str = "abc" + str
        str_hash = hashlib.sha256(str.encode('utf-8')).hexdigest()
        return str_hash

    # generate key pairs(y)
    def create_key_pairs_by_length(self, key_length):
        # Use RSA to generate user key pairs
        KeyPair = RSA.generate(bits=key_length)

        private_key = "file/private_key.pem"
        with open(private_key, 'wb') as fpri:
            fpri.write(KeyPair.exportKey("PEM"))
            fpri.close()

        public_key = "file/public_key.pem"
        with open(public_key, 'wb') as fpub:
            fpub.write(KeyPair.publickey().exportKey("PEM"))
            fpub.close()
        return {"private_key": private_key, "public_key": public_key}

    def new_keyPairs(self, key_length):
        return KeyPairs(self.create_key_pairs_by_length(key_length), key_length)

    # (y)
    def __init__(self, username, password, wallet_key="", email="", phone_number="") -> None:
        self._username = username
        self._password = self.encodeByHash(password)
        self._wallet_key = wallet_key
        self._email = email
        self._phone_number = phone_number
        self._keypairs = None
        self._photo = "file/DefaultPhoto.jpg"
        self._message = []
        self._private_key_location = ""

    # def __init__(self, username, password) -> None:
    #     self._username = username
    #     self._password = self.encodeByHash(password)

    def get_private_key_location(self) -> list:
        return self._private_key_location

    def set_private_key_location(self, private_key_location) -> None:
        self._private_key_location = private_key_location

    def get_message(self) -> list:
        return self._message

    def set_message(self, message) -> None:
        self._message = message

    def get_photo(self) -> bytes:
        return self._photo

    def set_photo(self, photo) -> None:
        self._photo = photo

    def get_keypairs(self) -> KeyPairs:
        return self._keypairs

    def set_keypairs(self, keypairs) -> None:
        self._keypairs = keypairs

    def get_phone_number(self) -> string:
        return self._phone_number

    def set_phone_number(self, phone_number) -> None:
        self._phone_number = phone_number

    def get_email(self) -> string:
        return self._email

    def set_email(self, email) -> None:
        self._email = email

    def get_wallet_key(self) -> string:
        return self._wallet_key

    def set_wallet_key(self, wallet_key) -> None:
        self._wallet_key = wallet_key

    def get_password(self) -> string:
        return self._password

    def set_password(self, password) -> None:
        self._password = self.encodeByHash(password)

    def get_username(self) -> string:
        return self._username

    def set_username(self, username) -> None:
        self._username = username
