#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import json
from sys import getsizeof
from hashlib import sha256


'''
for the future
    BLOCK STRUCTURE :
BLOCK SIZE > size in MB
BLOCK HEADER > version, previous_hash, merkle_tree_root, timestamp, nonce
DATA HEADER > number_of_transactions
DATA : transactions
'''

class Block(object):

    def __init__(self, index, previous_hash, timestamp, difficulty, nonce, transactions):
        #Size
        self.size = 0 #int
        #Header
        self.index = index #int
        self.previous_hash = previous_hash #str
        self.merkle_root = None #str
        self.timestamp = timestamp #int
        self.difficulty = difficulty #str
        self.nonce = nonce #bytes
        #Transaction count
        self.number_of_transactions = 0 #int
        #Transactions
        self.transactions = transactions #str json.dumps() '[{tx01},...,{txN}]'

    def calculate_size(self):
        # NOTE: migth be unnecessary done by pick_transactions()
        return

    def verify_block(block):
        '''Verify the block is valid for a given difficulty'''
        sha=sha256((str(block.index)
                    + block.previous_hash
                    + str(block.timestamp)
                    + block.difficulty
                    + str(block.nonce)
                    ).encode('utf-8')
                   ).hexdigest()
        if int(sha, 16) > target(block.difficulty):
            raise InvalidBlock

if __name__ == '__main__':
    pass
