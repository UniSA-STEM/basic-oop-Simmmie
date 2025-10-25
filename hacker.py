"""
File: hacker.py
Description: <A brief description of this Python module.>
Author: Simone Pericic
ID: 110085418
Username: Persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import *
from rig import Rig


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
        self.__inventory = []
        self.__rig = rig
        self.__trace_level = trace_level
        self.__starting_inventory()

    def __starting_inventory(self):
        """ Hackers starting assets - 1 CryptoToken"""
        return self.__inventory.append(create_crypto_token())

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory.copy()

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    def get_max_trace(self):
        return self.__MAX_TRACE

    def __check_trace_level(self):
        if self.__trace_level <= self.__MAX_SAFE_TRACE:
            return True
        else:
            return False

    def has_rig(self):
        return self.__rig is not None

    def gain_rig(self, rig):
        if self.__rig is not None:
            print(f'\n{self.__name} already has a rig. Cannont acquire another rig.')
            return False
        elif self.scan_inventory('cryptoToken') is None:
            print(f'\n{self.__name} needs a Crypto Token to gain a new rig.')
            return False
        elif self.__rig is None:
            self.__rig = rig
            print(f'\nNew rig acquired.')
            print(f'Rig is online and functional. ')
            return True

    def use_data_spike(self, target_rig):
        if self.__rig is None:
            print(f'{self.__name} has no rig to launch attacks.')
            return False
        elif not self.__check_trace_level():
            print(f'Trace level is too high {self.__trace_level}.'
                  f'Reduce trace level before attacking.'
                  f'Max safe level: {self.__MAX_SAFE_TRACE}.')
            return False
        else:
            target_rig.take_hit()
            self.__trace_level += self.__TRACE_ATTACK
            print(f'{self.__name} launced a Data Spike at {target_rig.get_name()}.'
                  f'\n Trace level increased: {self.__trace_level} / {self.__MAX_SAFE_TRACE}')
            return True

    def extract_assets(self, target_rig):
        drive = self.scan_inventory('Removable Drive')

        if self.__rig is None:
            print(f'{self.__name} needs a rig to extract assets.')
            return False
        elif not target_rig.if_broken():
            print(f'{target_rig.get_name()} must be broken to extract assets.'
                  f'\n Current condition: {target_rig.get_condition()}')
            return False
        elif drive is None:
            print(f'{self.__name} needs a Removeable Drive to extract assets.')
            return False
        else:
            extracted_assets = target_rig.extract_all_unecrypted()
            for asset in extracted_assets:
                self.__inventory.append(asset)

            self.__trace_level += self.__TRACE_EXTRACT
            print(f'{self.__name} extracted {len(extracted_assets)} assets.'
                  f'\n Trace level increased: {self.__trace_level} / {self.__MAX_SAFE_TRACE}')
            return True

    def encrypt_assets(self, asset_name, location = 'inventory'):
        chip = self.scan_inventory('Security Chip')
        if chip is None:
            print(f'{self.__name} needs a Security Chip to encrypt assets.')
            return False

        asset = None

        if location == 'inventory':
            asset = self.__find_asset_inventory(asset_name)
            if asset is None:
                print(f'{asset_name} not found in inventory.')
                return False
        elif location == 'rig':
            if self.__rig is None:
                print(f'{self.__name} need a rig to encrypt assets in rig storage.')
                return False

            found = False
            for rig_asset in self.__rig.get_storage():
                if rig_asset.get_name() == asset_name and not found:
                    asset = rig_asset
                    found = True

            if asset is None:
                print(f'{asset_name} not found in rig storage.')
                return False
        else:
            print(f'\nInvalid location: {location}')
            return False

        if asset.is_encrypted():
            print(f'{asset_name} is already encrypted')
            return False

        asset.set_encrypted(True)
        print(f'{asset_name} encrypted in {location}.'
              f'\n Asset is now protected from theft.)
        return True

    def decrypt_assets(self, asset_name, location = 'inventory'):
        chip = self.scan_inventory('Security Chip')
        if chip is None:
            print(f'{self.__name} needs a Security Chip to decrypt assets.')
            return False

        asset = None

        if location == 'inventory':
            asset = self.__find_asset_inventory(asset_name)
            if asset is None:
                print(f'{asset_name} not found in inventory.')
                return False
        elif location == 'rig':
            if self.__rig is None:
                print(f'{self.__name} need a rig to decrypt assets in rig storage.')
                return False

            found = False
            for rig_asset in self.__rig.get_storage():
                if rig_asset.get_name() == asset_name and not found:
                    asset = rig_asset
                    found = True

            if asset is None:
                print(f'{asset_name} not found in rig storage.')
                return False
        else:
            print(f'\nInvalid location: {location}')
            return False

        if asset.is_encrypted():
            print(f'{asset_name} is not encrypted')
            return False

        asset.set_encrypted(False)
        print(f'{asset_name} decrypted in {location}.'
              f'\n Asset is now be transferred.)
        return True

    def upgrade_rig(self):
        patch = self.scan_inventory('Hardware Patch')
        if self.__rig is None:
            print(f'{self.__name} needs a rig to upgrade.')
            return False
        elif patch is None:
            print(f'{self.__name} needs a Hardware Patch to upgrade rig.')
            return False
        else:
            return self.__rig.upgrade(patch)

    def store_in_rig(self, asset_name):
        if self.__rig is None:
            print(f'{self.__name} needs a rig to store assets into.')
            return False

        asset = self.__find_asset_inventory(asset_name)
        if asset is None:
            print(f'{asset_name} not found in inventory.')
            return False

        self.__remove_asset_inventory(asset)
        success = self.__rig.store_asset(asset)

        if not success:
            self.__inventory.append(asset)
        else:
            return success

    def retrieve_from_rig(self, asset_name):
        if self.__rig is None:
            print(f'{self.__name} needs a rig to retrieve assets.')
            return False

        asset = self.__rig.send_asset(asset_name)

        if asset is None:
            return False

        self.__inventory.append(asset)
        print(f'{asset_name} sent to inventory.')
        return True

    def store_all_in_rig(self, asset_name):
        if self.__rig is None:
            print(f'{self.__name} needs a rig.')
            return False

        count = 0
        inventory_copy = self.__inventory.copy()

        for asset in inventory_copy:
            if self.__rig.get_storage() <self.__rig.get_max_storage():
                self.__remove_asset_inventory(asset)
                if self.__rig.store_assets(asset):
                    count += 1
                else:
                    self.__inventory.append(asset)

        print(f'Stored {count} assets in rig.')
        return True

    def retrieve_all_in_rig(self):
        if self.__rig is None:
            print(f'{self.__name} needs a rig.')
            return False

        count = 0
        storage_copy = self.__rig.get_storage()

        for asset in storage_copy:
            if not asset.is_encrypted():
                sent = self.__rig.send_asset(asset.get_name())
                if sent:
                    self.__inventory.append(sent)
                    count += 1

        print(f'Sent {count} assets to the inventory.')
        return True

    def __find_asset_inventory(self, asset_name):
        for asset in self.__inventory:
            if asset.get_name() == asset_name:
                return asset
        return None

    def __remove_asset_inventory(self, asset):
        if asset in self.__inventory:
            self.__inventory.remove(asset)

    def scan_inventory(self, asset_name):
        asset = self.__find_asset_inventory(asset_name)
        if asset:
            self.__remove_asset_inventory(asset)
        return asset

    def reduce_trace_level(self, amount = 1):
        self.__trace_level = max(0, self.__trace_level - amount)
        print(f'{self.__name} reduced trace by {amount}'
              f'Current trace level: {self.__trace_level}')

    def __str__(self):
        rig_name = self.__rig.name if self.__rig else 'None'
        return (f'\nHacker: {self.__name} '
                f'\nRig: {rig_name}'
                f'\nTrace {self.__trace_level} / {self.__MAX_SAFE_TRACE}'
                f' \nInventory: {self.__inventory}')


    name = property(get_name)
    inventory = property(get_inventory)
    rig = property(get_rig)
    trace_level = property(get_trace_level)