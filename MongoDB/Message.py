from datetime import datetime
import string


class Message:
    def __init__(self, sender, receiver, message_type, message, delivery_type) -> None:
        self._sender = sender
        self._receiver = receiver
        self._message_type = message_type
        self._message = message
        self._timestamp = datetime.now()
        self._delivery_type = delivery_type

    def get_delivery_type(self) -> string:
        return self._delivery_type

    def set_delivery_type(self, delivery_type) -> None:
        self._delivery_type = delivery_type

    def get_timestamp(self):
        return self._timestamp

    def set_timestamp(self, timestamp) -> None:
        self._timestamp = timestamp

    def get_message(self):
        return self._message

    def set_message(self, message) -> None:
        self._message = message

    def get_message_type(self) -> string:
        return self._message_type

    def set_message_type(self, message_type) -> None:
        self._message_type = message_type

    def get_receiver(self) -> string:
        return self._receiver

    def set_receiver(self, receiver) -> None:
        self._receiver = receiver

    def get_sender(self) -> string:
        return self._sender

    def set_sender(self, sender) -> None:
        self._sender = sender
