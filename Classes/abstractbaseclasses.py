from abc import ABC, abstractmethod


class invalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise invalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise invalidOperationError("Stream is already close.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream")


stream = MemoryStream()
stream.open()
