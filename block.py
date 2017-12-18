#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
for the future
    BLOCK STRUCTURE :
BLOCK SIZE > size in MB
BLOCK HEADER > version, index, timestamp, nonce, previous_hash
DATA HEADER > number_of_transactions, merkle_tree_root
DATA : transactions
'''

class Block():
    def __init__(self, index, timestamp, previous_hash, nonce, data):
        self.index=index
        self.timestamp=timestamp
        self.previous_hash=previous_hash
        self.nonce=nonce
        #self.merkle_tree_root
        #self.number_of_transactions
        self.data=data
