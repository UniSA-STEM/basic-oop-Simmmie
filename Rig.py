"""
File: Rig.py
Description: Rig class to emulate the hackers rig (computer) system.
Author: Simone Pericic
ID: 110085418
Username: persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name, damage = 0, status = False, storage, upgrade_level = 0, max_storage = 5, damage_threshold = 2):
        self.__name = name
        self.__damage = damage
        self.__status = status
        self.__storage = storage
        self.__upgrade_level = upgrade_level
        self.__max_storage = max_storage
        self.__damage_threshold = damage_threshold

    def get_name(self):
        return self.__name

    def set_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def if_broken(self):

    def get_storage(self):
        return self.__storage

    def get_upgrade_level(self):
        return self.__upgrade_level

    def get_max_storage(self):
        return self.__max_storage

    def __


    def get_damage_level(self):
        return self.__damage_level

    def repair(self, cyrpto_token):
        #TODO: repair using cyrpto token, cost 1

    def upgrade(self, hardware_patch):
        #TODO: upgrade using hardware patch

    def damage_hit(self):
        #TODO: take damage - hit

    def __generate_assets(self):
        #TODO: Generate random assests over time.

    def __starting_assets(self, crypto_token):
        #TODO: one crypto token as starting asset

    def store_assets(self):
        # TODO: asset storage flesh out.

    def __find_assets(self):

    def take_unencrypted(self):
        #TODO: emulate breach of unencrypted data being taken.

    def __str__(self):
    #TODO: display string.

