""" Wrappers for common comms interfaces

Classes:
    - Comms: Abstract base class for all comms classes
    - SerialSettings
    - SerialComms
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

from serial import Serial


class Comms(ABC):
    """ Base comms interface
    Methods:
        - open
        - close
        - write
        - read
    """

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def read(self, num_bytes):
        pass


@dataclass
class SerialSettings:
    """Settings for configuring serial"""
    port: str = None
    baud_rate: int = 9600

    @classmethod
    def create_from_config(cls, config: dict):
        """ Construct from configuration dictionary """
        return cls(config['port'], config['baud_rate'])


class SerialComms(Comms):
    """ Serial comms wrapper, inherits from Comms interface class """

    def __init__(self, settings: SerialSettings):
        self.comms_object = Serial()
        self.comms_object.port = settings.port
        self.comms_object.baudrate = settings.baud_rate

    def open(self):
        """@override"""
        self.comms_object.open()
        
    def close(self):
        """@override"""
        self.comms_object.close()

    def write(self, data):
        """@override"""
        self.comms_object.write(data)

    def read(self, num_bytes):
        """@override"""
        return self.comms_object.read(num_bytes)


# Maybe use this for functional testing of the classes in this file,
# not sure if this is good practice though
if __name__ == '__main__':
    pass
