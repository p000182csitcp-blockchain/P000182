import string
from click import password_option
from MongoDB.KeyPairs import KeyPairs


class User:
    def encodeByHash(str) -> string:
        return None

    def create_key_pairs_by_length(key_length) -> dict:
        return None

    def __init__(self, username, password, wallet_key, email, phone_number, key_length, photo=None):
        self._username = username
        self._password = self.encodeByHash(password)
        self._phone_number = phone_number
        self._email = email
        self._photo = photo
        self._wallet_key = wallet_key
        self._keypairs = KeyPairs(self.create_key_pairs_by_length, key_length)
        self._message = []

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
