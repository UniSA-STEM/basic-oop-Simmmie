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
        if self.__status is False:
            print(f'{self.__name} Pristine (Level {self.__damage_max}.')
        elif self.__status is True and self.__damage is not == self.__damage_max:
            print

            print(f'{self.__name} Broken (Level 0).')

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

    def calculate_damage_max(self):
        self.__damage_max = self.__STARTING_DAMAGE +(self.__upgrade_level * self.__STORAGE_PER_LEVEL)

    def __calculate_max_storage(self):
        self.__max_storage = self.__STARTING_STORAGE + (self.__upgrade_level * self.__ADDITION_DAMAGE_LEVELUP)

    def get_damage_max(self):
        return self.__damage_max

    def repair(self, crypto_token):
        if crypto_token.name != 'CryptoToken':
            raise ValueError('Repair requires a CryptoToken.')
        elif self.__damage == 0 and not self.__status:
            print(f'{self.__name} is not damaged, no repairs needed.')
        else:
            self.__damage =0
            self.__status = False
            print(f'{self.__name} has been repaired.')

    def upgrade(self, hardware_patch):
        if hardware_patch.name != 'Hardware Patch':
            raise ValueError(f'Upgrade requires a Hardware Patch.')
        else:
            self.__upgrade_level += 1
            self.__max_storage += 1
            self.__damage_max =
            print(f'{self.__name} upgraded to level {self.__upgrade_level}.')

    def damage_hit(self):
        if not self.__status:
            self.__damage += 1
            if self.__damage >= self.__damage_max:
                self.__status = True
            else:
                print(f'{self.__name} took a hit, damage: {self.__damage}.')

    def __generate_assets(self):
        #TODO: Generate random assests over time.

    def __starting_assets(self, crypto_token):
        #TODO: one crypto token as starting asset

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

    name = property(get_name, set_name)
    damage = property(get_damage)
    status = property(status)
    storage = property(get_storage)
    upgrade_level = property(get_upgrade_level)
    max_storage = property(get_max_storage)
    damage_max= property(get_damage_max)
