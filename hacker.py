"""
File: hacker.py
Description: <A brief description of this Python module.>
Author: Simone Pericic
ID: 110085418
Username: Persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
from rig import Rig

#TODO: work out why import from rig isnt working!!


class Hacker:
    """
    Emulates a hacker with an inventory, rig, data extraction, attacks and
    trace level. Can attack other rigs to try steal unencrypted data and
    be attacked in return.
    """

    __MAX_SAFE_TRACE = 5                # Max for safe trace level.
    __TRACE_ATTACK = 1                  # Trace gained from attack.
    __TRACE_EXTRACT = 2                 # Trace Gained from extraction.


    def __init__(self, name, rig = None, trace_level = 0):
        self.__name = name
        self.__inventory = self.__starting_inventory()
        self.__rig = rig
        self.__trace_level = trace_level

    def __starting_inventory(self):
        """ Hackers starting assets - 1 CryptoToken"""
        return self.__inventory.append(Asset.create_crypto_token())

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def current_trace_level(self, trace_level):
        #TODO: starts at 0 / NONE
        return self.__trace_level

    def gain_rig(self, rig):
        if self.__rig is not None:
            print(f'{self.__name} already has a rig. Cannont acquire another rig.')
        elif self.scan_inventory('crypto_token') is None:
            print(f'{self.__name} needs a Crypto Token to gain a new rig.')
        elif self.__rig is None:
            self.__rig = rig
            print(f'New rig acquired')

    def use_data_spike(self):
        #TODO: attack another rig (increases trace, comsumes data spike.

    def extract_assets(self):
        #TODO: Steals unencrypted assests broken rigs, consumes removable drive

    def encrypt_assets(self):
        #TODO: encrypts assets inventory  or rig (uses security chip)

    def decrypt_assts(self):
        #TODO: Decrypt asset uses security chip

    def upgrade_rig(self):
        #TODO: upgrades hackers rig - hardware patch
        return self.__rig

    def store_in_rig(self, asset_name):
        #TODO: transfers assests from inventory to rig storage.

    def retrieve_from_rig(self, asset_name):
        #TODO: transfers asset from inventory rig to hacker inventory.

    def store_all_in_rig(self, asset_name):

    def retreive_all_in_rig(self, asset_name):

    def scan_inventory(self, asset_name):
        #TODO: need to scan and remove select or all items.
        for asset in self.__inventory:
            if asset.name == asset_name:
                return asset
        return None

    def reduce_trace_level(self, amount):
        return self.__trace_level


    def __str__(self):
        rig_name = self.__rig.name if self._-rig else 'None'
        return (f'Hacker: {self.__name}, Rig: {rig_name},'
                f'\nTrace {self.__trace_level}, Inventory: {}')


    name = property(get_name)
    inventory = property(get_inventory)
    rig = property(get_rig)
    trace_level = property(get_trace_level)