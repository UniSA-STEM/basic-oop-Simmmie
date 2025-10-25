"""
File: main.py
Description: <A brief description of this Python module.>
Author: Simone Pericic
ID: 110085418
Username: Persn001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from hacker import *
from rig import *
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

    print('\n*** Potato launches an attack ***\n ')

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

    print('\n *** Creating hacker: Morty')
    morty = Hacker('Morty')
    morty.gain_rig()

    morty.get_inventory().append(create_hardware_patch())
    morty.get_inventory().append(create_hardware_patch())
    morty.get_inventory().append(create_hardware_patch())

    print('\n*** Rig status: ***')
    print(morty.get_rig())

    print('\n*** Upgrade 1 ***')
    morty.upgrade_rig()

    print('\n*** Upgrade 2 ***')
    morty.upgrade_rig()

    print('\n*** Upgrade 3 ***')
    morty.upgrade_rig()

    print('\n*** Upgrade 4 ***')
    morty.upgrade_rig()

    print('\n *** testing increaseing damage maximum ***')
    print('Level 3 rig should take 5 hits to break\n')

    rick = Hacker('Rick the Attacker')
    rick.gain_rig()

    for number in range(4):
        rick.get_rig().store_assets(create_data_spike())

    print('\n*** Starting attacks on the rig ***')
    for i in range(4):
        print(f'---- Attack {i + 1} ---')
        rick.use_data_spike(morty.get_rig())
        print()

def test_trace_level():
    print_sep('Test no 6: Trace level')

    print('\n *** Creating hacker: Over Byte')
    over_byte= Hacker('Over Byte')
    over_byte.gain_rig()

    for number in range(10):
        over_byte.get_rig().store_assets(create_data_spike())

    target_rig = Rig('Target Rig')

    print('\n *** Starting attacks to test trace level increase')

    for i in range(7):
        print(f'---- Attack {i + 1} ---')
        result = over_byte.use_data_spike(target_rig)

        if not result:
            print('\n Attack blocked due too high trace level')
        print()
    print(f'\n*** Current trace level: {over_byte.get_trace_level} / {over_byte.get_max_trace} ***')

    print('\n *** reducing trace level ***')
    over_byte.reduce_trace_level(3)

    print('\n *** Attempting attack after trace level reduction ***')
    over_byte.use_data_spike(target_rig)

    print('\n *** Final status: ***')
    print(over_byte)

def test_edge_cases():
    print_sep('Test no 7: Edge cases')

    print('\n*** Creating hacker: Edgy Egg')
    edgy_egg = Hacker('Edgy Egg')

    print('\n *** Test: attempt update without rig ***')
    edgy_egg.get_inventory().append(create_hardware_patch())
    edgy_egg.upgrade_rig()

    print('\n*** Test: Encrypt without Secutiry Chip ***')
    edgy_egg.get_inventory().append(create_crypto_token())
    edgy_egg.encrypt_assets("CryptoToken", 'inventory')

    print('\n*** Test: Gain rig then try to get another one ***')
    edgy_egg.gain_rig()
    print()
    edgy_egg.gain_rig()
    print()

    print('\n *** Test: Attacking without Data Spike ***')
    target_rig = Rig('Target Rig')

    edgy_egg.get_rig().send_asset('Data Spike')
    edgy_egg.get_rig().send_asset('Data Spike')
    print()
    edgy_egg.use_data_spike(target_rig)

    print('\n *** Extract from working rig ***')
    edgy_egg.get_inventory().append(create_removable_drive())
    edgy_egg.extract_assets(target_rig)

    print('\n *** Test: Repair undamaged rig **')
    edgy_egg.get_inventory().append(create_crypto_token())
    crypto = edgy_egg.scan_inventory('CryptoToken')
    edgy_egg.get_rig().repair(crypto)

    print('\n *** Test: store asset in full rig **')
    print('Filling rig storage to max level')
    for i in range(10):
        edgy_egg.get_rig().store_assets(create_data_spike())
        print('\n *** Attempting to store more ***')
        edgy_egg.get_rig().store_assets(create_crypto_token())

    print('\n *** Test: Gain rig without CryptoToken **')
    broke = Hacker('Broky Hacker')
    broke.scan_inventory('CryptoToken')
    broke.gain_rig()

def test_complex():
    print_sep('Test no 8')

    print('\n *** Corpo Heist'
          '\n Two hackers compete take the data.')

    print('\n *** Setting up hackers **')
    hacker1 = Hacker('Soap')
    hacker2 = Hacker('Goat')

    hacker1.gain_rig()
    hacker2.gain_rig()

    print('\n *** Hackers gathering assets ***')
    hacker1.get_inventory().append(create_hardware_patch())
    hacker1.get_inventory().append(create_security_chip())
    hacker2.get_inventory().append(create_hardware_patch())
    hacker2.get_inventory().append(create_security_chip())

    print('\n *** Soap upgrading rig ***')
    hacker1.upgrade_rig()
    hacker1.upgrade_rig()

    print('\n *** Goat upgrading rig ***')
    hacker1.upgrade_rig()

    print('\n *** Soap encrypting assets ***')
    hacker1.get_inventory().append(create_crypto_token())
    hacker1.get_inventory().append(create_crypto_token())
    hacker1.store_in_rig('CryptoToken')
    hacker1.encrypt_assets('CryptoToken', 'rig')

    print('\n *** Goat encrypting assets ***')
    hacker2.get_inventory().append(create_crypto_token())
    hacker2.store_in_rig('CryptoToken')
    hacker2.encrypt_assets('CryptoToken', 'rig')

    print('\n' + '=' * 60)
    print('\n *** Starting Battles ***')
    print('=' * 60 + '\n')

    print('\n *** Soap attacks Ghost\'s rig ***')
    hacker1.use_data_spike(hacker2.get_rig())
    hacker1.use_data_spike(hacker2.get_rig())
    hacker1.use_data_spike(hacker2.get_rig())
    hacker1.use_data_spike(hacker2.get_rig())

    print('\n *** Soap attempts to extract data ***')
    hacker1.get_inventory().append(create_removable_drive())
    hacker1.extract_assets(hacker2.get_rig())

    print('\n' + '=' * 60)
    print('\n *** Results of Battles ***')
    print('=' * 60 + '\n')

    print('\n Winner: Soap')
    print(hacker1)
    print(hacker1.get_rig())

def test_asset_gen():
    print_sep('Test no 9: Asset generation')

    print('\n *** Creating hacker: Poww')
    pow_w = Hacker('Poww')
    pow_w.gain_rig()

    print('\n *** Rig status: ***')
    print(pow_w.get_rig())

    print('\n *** Generating 5 random assets ***')
    for i in range(5):
        print(f'Generation number {i + 1}')
        pow_w.get_rig().generate_assets()
        print()

    print('\n *** Rig status: ***')
    print(pow_w.get_rig())

    print('\n *** Attempting to generate when storage is full ***')
    pow_w.get_rig().generate_assets()

def test_repair():
    print_sep('Test no 10: Repairing rig')

    print('\n *** Creating hacker: Crane')
    crane = Hacker('Crane')
    crane.gain_rig()

    attacker = Hacker('Baron')
    attacker.gain_rig()

    print('\n *** Attacking Crane\'s rig ***')
    attacker.use_data_spike(crane.get_rig())

    print('\n *** Rig status: ***')
    print(crane.get_rig())

    print('\n *** Repairing rig ***')
    crane.get_inventory().append(create_crypto_token())
    crypto = crane.scan_inventory('CryptoToken')
    crane.get_rig().repair(crypto)

    print('\n *** Rig status: ***')
    print(crane.get_rig())

if __name__ == '__main__':
    print('\n' + '=' * 60)
    print('=' + ' ' * 12 + "Comprehensive Test Suite" + ' ' * 22 + '=')
    print('=' * 60)

test_basic()
test_asset_management()
test_battles()
test_upgrading()
test_encryption()
test_trace_level()
test_edge_cases()
test_complex()
test_asset_gen()
test_repair()

print('\n' + '=' * 60)
print('=' + ' ' * 15 + "All tests complete" + ' ' * 25 + '=')
print('=' * 60)
