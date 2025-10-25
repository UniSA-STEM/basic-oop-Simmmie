"""
File: main.py
Description: <A brief description of this Python module.>
Author: Simone Pericic
ID: 110085418
Username: Persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from hacker import Hacker
from rig import Rig
from asset import *

"""
Main testing suite for indepth testing of the program.
"""
def print_sep(title = ''):
    if title:
        print(f'\n{'=' * 60}')
        print(f' {title}')
        print(f'{'=' * 60}\n')
    else:
        print(f'\n{'=' * 60}\n')

def test_basic():
    print_sep('Test no 1: Basic Layout')

    print('*** Creating Hackers ***')
    name = Hacker('Sir Fuffles')
    name2 = Hacker('Mad hatter')

    print(name)
    print()
    print(name2)

    print('\n*** Gaining Rigs ***')
    name.gain_rig()
    print()
    name2.gain_rig('Mad hatters crazy rig.')

    print('\n *** End status: ***')
    print(name)
    print(name2)
    print()

    print('\n*** Rig details.. ***')
    print(name.get_rig())
    print(name2.get_rig())
    print()

def test_asset_management():
    print_sep('Test no 2: Asset management')

    print('\n *** Creating hacker: Dango ***')
    dango = Hacker('Dango')
    dango.gain_rig()

    print('\n*** Adding assets to inventory ***')
    dango.get_inventory().append(create_security_chip())
    dango.get_inventory().append(create_hardware_patch())
    dango.get_inventory().append(create_crypto_token())
    print('Added Secrutiy chip, hardware patch and CryptoToken')
    print(dango)

    print('\n *** Storing asset in the rig ***')
    dango.store_in_rig('Security Chip')
    print()
    dango.store_in_rig('Hardware Patch')

    print('\n Current rig status: ***')
    print(dango.get_rig())

    print('\n *** Getting Hardware Patch from the rig ***')
    dango.retrieve_from_rig('Hardware Patch')

    print('\n*** Final Status: ***')
    print(dango)

def test_battles():
    print_sep('Test no 3: Battle System' )

    print('\n *** Setting up battle ***')
    potato = Hacker('Potato')
    potato.gain_rig()
    target_rig = Rig('Maz\'s Rig')

    print('Attacker:')
    print(potato)
    print('Target:')
    print(target_rig)

    print('\n*** Potatoo launches an attack ***\n ')

    print('--- Attack 1 ---')
    potato.use_data_spike(target_rig)

    print('\n--- Attack 2 ---')
    potato.use_data_spike(target_rig)

    print('\n *** Target rigs condition ****')
    print(target_rig)

    print('\n *** Attempting extraction ***')
    potato.get_inventory().append(create_removable_drive())
    potato.extract_assets(target_rig)

    print('\n*** Final status: ***')
    print(potato)
    print(target_rig)
    print()

def test_encryption():
    print_sep('Test no 4: Encryption')

    print('\n*** Creating hacker: Soggy Bytes ***')
    soggy_bytes = Hacker('Soggy Bytes')
    soggy_bytes.gain_rig()

    soggy_bytes.get_inventory().append(create_security_chip())
    soggy_bytes.get_inventory().append(create_crypto_token())
    soggy_bytes.get_inventory().append(create_hardware_patch())
    soggy_bytes.get_inventory().append(create_security_chip())
    soggy_bytes.get_inventory().append(create_security_chip())

    print('\n *** Starting Inventory ****')
    print(soggy_bytes)

    print('\n *** Encrypting Hardware Patch in inventory ***')
    soggy_bytes.encrypt_assets('Hardware Patch', 'Inventory')

    print('\n*** Storing CryptoToken in the rig ***')
    soggy_bytes.store_in_rig('CryptoToken')

    print('\n*** Encrypting CryptooToken in the rig ***')
    soggy_bytes.encrypt_assets('CyrptoToken', 'rig')

    print('\n *** Current status: ***')
    print(soggy_bytes)

def test_upgrading():
    print_sep('Test no 5: Upgrading System')

    print('\n *** Creating hacker: ')


