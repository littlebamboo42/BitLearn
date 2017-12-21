#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
for the future
    BLOCK STRUCTURE :
BLOCK SIZE > size in MB
BLOCK HEADER > version, previous_hash, merkle_tree_root, timestamp, nonce
DATA HEADER > number_of_transactions
DATA : transactions
'''

class Block():
    def __init__(self, index, previous_hash, timestamp, difficulty, nonce, data):
        #Size - 4 bytes
        #self.block_size=size
        #Header - 80 bytes
        self.version=1
        self.index=index#for now only, needs removal
        self.previous_hash=previous_hash
        #self.merkle_tree_root
        self.timestamp=timestamp
        self.difficulty=difficulty
        self.nonce=nonce
        #Transaction count - 1~9 bytes
        #self.number_of_transactions
        #Transactions - 999907~999915 bytes (100000-4-80-1~9)
        self.data=data
