import string


class KeyPairs:
    def __init__(self, keypairs, length) -> None:
        self._keypairs = keypairs
        self._length = length

    def get_length(self) -> string:
        return self._length

    def set_length(self, length) -> None:
        self._length = length

    def get_keypairs(self) -> dict:
        return self._keypairs

    def set_keypairs(self, keypairs) -> None:
        self._keypairs = keypairs
