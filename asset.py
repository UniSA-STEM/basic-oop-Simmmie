"""
File: asset.py
Description: Asset class to emulate the digital assests used by rigs and hackers.
Author: Simone Pericic
ID: 110085418
Username: persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""



class Asset:
    """
    the Asset class: represetns the digital assets, each asset has a name,
    description and encryption status.
    """

    def __init__(self, name, description, encrypted = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def is_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, status):
        if not isinstance(status, bool):
            raise ValueError('Encryption status must be boolean.')
        else:
            self.__encrypted = status

    def __str__(self):
        if self.__encrypted:
            return f'{self.__name}: {self.__description} [Encrypted].'
        else:
            return f'{self.__name}: {self.__description}'

    name = property(get_name)
    description = property(get_description)
    encrypted = property(is_encrypted, set_encrypted)


def create_crypto_token():
        return Asset('CryptoToken', 'Digital currency for purchases and repairs to rigs.')

def create_data_spike():
        return Asset('Data Spike', 'Program for attacking other rigs.')

def create_removable_drive():
        return Asset('Removable Drive', 'Storage device for extracting assets.')

def create_security_chip():
        return Asset('Security Chip', 'Tool for encrypting and decrypting assets.')

def create_hardware_patch():
        return Asset('Hardware Patch', 'Part for upgrading rigs.')


