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

    __STARTING_STORAGE = 5
    __STARTING_DAMAGE = 2
    __STORAGE_PER_LEVEL = 2
    __ADDITION_DAMAGE_LEVELUP = 1

    def __init__(self, name, damage = 0, condition = False, upgrade_level = 0, max_storage = 5, damage_max = 2):
        self.__name = name
        self.__damage = damage
        self.__condition = condition
        self.__storage = []
        self.__upgrade_level = upgrade_level
        self.__max_storage = max_storage
        self.__damage_max = damage_max

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def condition(self):
        # returns True if rig is broken
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
        self.__max_storage = self.__STARTING_STORAGE + (self.__upgrade_level * self.__ADDITION_DAMAGE_LEVELUP)

    def __find_asset_by_name(self):
        for asset in self.__storage:
            if asset.get_name() == name:
                return asset
        return None

    def get_damage_max(self):
        return self.__damage_max

    def __calculate_damage_max(self):
        self.__damage_max = self.__STARTING_DAMAGE +(self.__upgrade_level * self.__STORAGE_PER_LEVEL)

    def repair(self, crypto_token):
        if crypto_token.name is None:
            print(f'Repair requires a CryptoToken to repair {self.__name}.')
            return False
        elif self.__damage == 0 and not self.__status:
            print(f'{self.__name} is not damaged, no repairs needed.')
            return False
        else:
            self.__damage =0
            self.__status = False
            print(f'{self.__name} has been repaired.')
            return True

    def upgrade(self, hardware_patch):
        if hardware_patch.name is None:
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

        if self.__damage >= self.__damage_max:
            self.__condition = True
            print(f'{self.__name} is now broken.'
                  '\nUnencrypted assets can now be stolen.')
            return True
        else:
            print(f'{self.__name} is still operational.'
                  f'\n Damage: {self.__damage} / {self.__damage_max}')
            return False

    def __generate_assets(self):
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
        print(f'{self.__name} generated: {asset.get.name()}.')
        print(f'Storage: {len(self.__storage)} / {self.__max_storage}.')
        return asset


    def store_assets(self, asset):
        if len(self.__storage) >= self.__max_storage:
            raise ValueError('Storage is full.')
        if asset.is_encrypted:
            raise ValueError('Cannont store encrypted assets.')
        self.__storage.append(asset)

    def __find_assets(self):

    def take_unencrypted(self):
        #TODO: emulate breach of unencrypted data being taken.

    def __str__(self):
        condition = 'Broken'if self.__status else f'Damage {self.__damage}/{self.__damage_max}'
        return (f'Rig: {self.__name}, Condition {condition},'
                f'Level: {self.__upgrade_level}, Storage: {}')

    if self.__status is False:
        print(f'{self.__name} Pristine (Level {self.__damage_max}.')
    elif self.__status is True and self.__damage is not == self.__damage_max:
        print

        print(f'{self.__name} Broken (Level 0).')


    name = property(get_name, set_name)
    damage = property(get_damage)
    status = property(status)
    storage = property(get_storage)
    upgrade_level = property(get_upgrade_level)
    max_storage = property(get_max_storage)
    damage_max= property(get_damage_max)
