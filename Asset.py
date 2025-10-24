"""
File: Asset.py
Description: Asset class to emulate the digital assests used by rigs and hackers.
Author: Simone Pericic
ID: 110085418
Username: persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Assets:
    def __init__(self, name, description, encrypted = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def if_encrypted(self):
        # TODO: Boolean if true = encrypted
        return self.__encrypted

    def set_encrypted(self, status):
        if not isinstance(status, bool):
            raise ValueError('Encryption status must be boolean.')
        else:
            return self.__encrypted


    def create_crypto_token(self):


    """
    poss create functions for

    data spike
    removable drive
    security chip
    hardware patch
    """

    def __str__(self):
        #TODO: string output

    name = property(get_name)
    description = property(get_description)
    encrypted = property(if_encrypted, set_encrypted)

