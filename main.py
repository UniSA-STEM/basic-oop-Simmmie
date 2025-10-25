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
from asset import Asset

# Test Consume crypto token and print message.
def test_rig_acquire():
    hacker = Hacker('SirFluffles')
    rig = Rig('Meeseeks')
    hacker.acquire_rig(rig)
    print(Hacker)