#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from genesis import *
from miner import *

#Create the blockchain and start it with the genesis block
blockchain = [create_genesis_block()]

#Size of the blochain to find
size = 5

#Start with the genesis block to mine
previous_block = blockchain[0]

#Lengthen the blockchain
for i in range(0, size):
    block_to_add = new_block(previous_block)
    blockchain.append(block_to_add)
    print('Block #{} has been added to the blockchain!'.format(block_to_add.index))
    print('Timestamp: {}'.format(str(block_to_add.timestamp)))
    print('Previous Hash: {}'.format(str(block_to_add.previous_hash)))
    previous_block = block_to_add
