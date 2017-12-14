#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from genesis import *
from miner import *

blockchain = [create_genesis_block()]

previous_block = blockchain[0]

#Size of the blochain
size = 5

# Add blocks
for i in range(0, size):
    block_to_add = new_block(previous_block)
    blockchain.append(block_to_add)
    print('Block #{} has been added to the blockchain!'.format(block_to_add.index))
    print('Timestamp: {}'.format(str(block_to_add.timestamp)))
    print('Hash: {}\n'.format(str(block_to_add.hash)))
    previous_block = block_to_add

print(blockchain)
