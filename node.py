#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from miner import *
from generate_key_pair import *

wallet=generate_key_pair()
print('k : {}\nA : {}'.format(wallet[0], wallet[2]))

#Size of the blochain to find in number of blocks including genesis block
size = 10

#Make a blockchain
blockchain=[]

previous_block=None

#Create and lengthen the blockchain
for i in range(0, size):
    block_to_add = new_block(previous_block)
    blockchain.append(block_to_add)
    print('Block #{} has been added to the blockchain!'.format(block_to_add.index))
    print('Timestamp: {}'.format(str(block_to_add.timestamp)))
    print('Previous Hash: {}'.format(str(block_to_add.previous_hash)))
    previous_block = block_to_add
