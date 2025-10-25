"""
File: rig.py
Description: Rig class to emulate the hackers rig (computer) system.
Author: Simone Pericic
ID: 110085418
Username: persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

import random
from asset import *


class Rig:

    """Rig class emulates a hackers computer (rig) system: maanages storage,
    damage, upgrades and asset generation over time"""

    __STARTING_STORAGE = 5                      # Starting storage max.
    __STARTING_DAMAGE = 2                       # Starting damage max.
    __STORAGE_PER_LEVEL = 2                     # Storage space increase per level up.
    __ADDITION_DAMAGE_LEVELUP = 1               # Damage max increase per levelup.

    def __init__(self, name, damage = 0, condition = False, upgrade_level = 0):
        self.__name = name
        self.__damage = damage
        self.__condition = condition
        self.__storage = []
        self.__upgrade_level = upgrade_level
        self.__max_storage = self.__STARTING_STORAGE
        self.__damage_max = self.__STARTING_DAMAGE
        self.__starting_assets()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_damage(self):
        return self.__damage

    def get_condition(self):
        # returns True if rig is broken default is False.
        return self.__condition

    def if_broken(self):
        if self.__damage >=self.__damage_max:
            self.__condition = True
        else:
            self.__condition = False

        return self.__condition

    def get_storage(self):
        return self.__storage

    def __starting_assets(self):
        self.__storage.append(create_data_spike())
        self.__storage.append(create_data_spike())
        self.__storage.append(create_removable_drive())

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_max_storage(self):
        return self.__max_storage

    def __calculate_storage_max(self):
        self.__max_storage = self.__STARTING_STORAGE + (self.__upgrade_level * self.__STORAGE_PER_LEVEL)

    def __find_asset_by_name(self, name):
        for asset in self.__storage:
            if asset.get_name() == name:
                return asset
        return None

    def get_damage_max(self):
        return self.__damage_max

    def __calculate_damage_max(self):
        self.__damage_max = self.__STARTING_DAMAGE +(self.__upgrade_level * self.__ADDITION_DAMAGE_LEVELUP)

    def repair(self, crypto_token):
        if crypto_token is None:
            print(f'Repair requires a CryptoToken to repair {self.__name}.')
            return False
        elif self.__damage == 0 and not self.__condition:
            print(f'{self.__name} is not damaged, no repairs needed.')
            return False
        else:
            self.__damage =0
            self.__condition = False
            print(f'{self.__name} has been repaired.')
            return True

    def upgrade(self, hardware_patch):
        if hardware_patch is None:
            print(f'Upgrade requires a Hardware Patch.')
            return False
        else:
            self.__upgrade_level += 1
            self.__calculate_storage_max()
            self.__calculate_damage_max()
            print(f'{self.__name} upgraded to level {self.__upgrade_level}.')
            print(f'Storage: {self.__max_storage}.'
                  f'\n Damage Maximum: {self.__damage_max}.')
            return True

    def damage_hit(self):
        if self.__condition:
            print(f'{self.__name} is already broken.')
            return False
        else:
            self.__damage += 1
            print(f'{self.__name} took a hit, Damage: {self.__damage} / {self.__damage_max}.')

        if self.if_broken():
            print(f'{self.__name} is now broken.'
                  '\nUnencrypted assets can now be stolen.')
            return True
        else:
            print(f'{self.__name} is still operational.'
                  f'\n Damage: {self.__damage} / {self.__damage_max}')
            return False

    def generate_assets(self):
        if len(self.__storage) >= self.__max_storage:
            print(f'{self.__name} storage is full ({self.__max_storage} / {self.__max_storage}).')
            print('Can\'t generate any more new assets.')
            return None

        assets_gen = [
            create_crypto_token,
            create_data_spike,
            create_removable_drive,
            create_security_chip,
            create_hardware_patch
        ]

        asset = random.choice(assets_gen)()
        self.__storage.append(asset)
        print(f'{self.__name} generated: {asset.get_name()}.')
        print(f'Storage: {len(self.__storage)} / {self.__max_storage}.')
        return asset


    def store_assets(self, asset):
        if asset is None:
            print(f'Cannot store invalid asset in {self.__name}')
            return False
        elif len(self.__storage) >= self.__max_storage:
            print(f'{self.__name} Storage is full.')
            return False
        else:
            self.__storage.append(asset)
            print(f'{asset.get_name()} stored in {self.__name}.')
            return True

    def send_asset(self, asset_name):
        asset = self.__find_asset_by_name(asset_name)

        if asset is None:
            print(f'{asset_name} not found in {self.__name} storage.')
            return None
        elif asset.is_encrypted():
            print(f'{asset_name} is encrypted and can\'t be transfered.'
                  '\nDecrypt the asset frist.')
            return None
        else:
            self.__storage.remove(asset)
            print(f'{asset_name} has been sent from {self.__name}.'
                  f'\nStorage: {len(self.__storage)} / {self.__max_storage}.')
            return asset

    def extract_all_unencrypted(self):
        extracted = []
        storage_copy = self.__storage.copy()

        for asset in storage_copy:
            if not asset.is_encrypted():
                extracted.append(asset)
                self.__storage.remove(asset)

        if len(extracted) > 0:
            print(f'Extracted {len(extracted)} unencrypted assets from {self.__name}')
            for asset in extracted:
                print(f'{asset.get_name()}')
        else:
            print(f'No unencrypted assets found in {self.__name}.')
        return extracted

    def __str__(self):
        if self.__condition:
            status = f'Broken {self.__damage} / {self.__damage_max}'
        elif self.__damage == 0:
            status = f'Pristine {self.__damage}/ {self.__damage_max}'
        else:
            status = f'Damaged {self.__damage} / {self.__damage_max}'

        storage_info = f'{len(self.__storage)} / {self.__max_storage}'
        return (f'Rig:          {self.__name}'
                f'\nCondition:  {status}'
                f'\nLevel:      {self.__upgrade_level}'
                f'\nStorage:    {storage_info}')


    name = property(get_name, set_name)
    damage = property(get_damage)
    condition = property(get_condition)
    storage = property(get_storage)
    upgrade_level = property(get_upgrade_level)
    max_storage = property(get_max_storage)
    damage_max= property(get_damage_max)
