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

    print('*** Creating Hackers ***\n')
    name = Hacker('Sir Fuffles')
    name2 = Hacker('Mad hatter')

    print(name)
    print()
    print(name2)

    print('\n*** Gaining Rigs ***\n')
    name.gain_rig()
    print()
    name2.gain_rig('Mad hatters crazy rig.\n')

    print('\n *** End status: ***\n')
    print(name)
    print(name2)
    print()

    print('\n*** Rig details.. ***\n')
    print(name.get_rig())
    print(name2.get_rig())
    print()

def test_asset_management():
    print_sep('Test no 2: Asset management')

    print('\n *** Creating hacker: Dango ***\n')
    dango = Hacker('Dango')
    dango.gain_rig()

    print('\n*** Adding assets to inventory ***\n')
    dango.get_inventory().append(create_security_chip())
    dango.get_inventory().append(create_hardware_patch())
    dango.get_inventory().append(create_crypto_token())
    print('Added Secrutiy chip, hardware patch and CryptoToken\n')
    print(dango)

    print('\n *** Storing asset in the rig ***\n')
    dango.store_in_rig('Security Chip')
    print()
    dango.store_in_rig('Hardware Patch')

    print('\n Current rig status: ***\n')
    print(dango.get_rig())

    print('\n *** Getting Hardware Patch from the rig ***\n')
    dango.retrieve_from_rig('Hardware Patch')

    print('\n*** Final Status: ***')
    print(dango)






