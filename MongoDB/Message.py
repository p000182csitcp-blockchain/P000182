import datetime
import string
import time


class Message:
    def __init__(self, sender, receiver, message_type, message, transport_type) -> None:
        self._sender = sender
        self._receiver = receiver
        self._message_type = message_type
        self._message = message
        self._timestamp = datetime.now()
        self._transport_type = transport_type

    def get_transport_type(self) -> string:
        return self._transport_type

    def set_transport_type(self, transport_type) -> None:
        self._transport_type = transport_type

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
