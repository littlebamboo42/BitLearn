#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from miner import *
from generate_key_pair import *
import json
import os

wallet=generate_key_pair()
print('k : {}\nA : {}'.format(wallet[0], wallet[2]))

#blockchain.json folder
location=''

previous_block=None

try:
    os.remove(location+'blockchain.txt')
except:
    pass

#Create and lengthen the blockchain
#while True: #main version
#for testing only
#Size of the blochain to find in number of blocks including genesis block
size = 10
for i in range(0, size):
    block_to_add = new_block(previous_block)
    with open(location+'blockchain.json','a') as blockchain:
        json.dump(vars(block_to_add), blockchain, indent=2)
    previous_block = block_to_add
