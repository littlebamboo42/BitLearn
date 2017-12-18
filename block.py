#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
for the future
    BLOCK STRUCTURE :
BLOCK SIZE > size in MB
BLOCK HEADER > version, index, timestamp, nonce, previous_hash, merkle_tree_root
DATA HEADER > number_of_transactions
DATA : transactions
'''

class Block():
    def __init__(self, index, timestamp, previous_hash, nonce, data):
        #Block size
        #self.block_size
        #Block header
        self.index=index
        self.timestamp=timestamp
        self.previous_hash=previous_hash
        self.nonce=nonce
        #self.merkle_tree_root
        #Block transaction header
        #self.number_of_transactions
        #Block transactions
        self.data=data
