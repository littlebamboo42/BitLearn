#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
Block format :
index
timestamp
previous hash
data
block hash
'''

import hashlib

class Block():
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = self.hash_block()

    def hash_block(self):
        sha3 = hashlib.sha3_256()
        sha3.update(str(self.index).encode('utf-8') +
                    str(self.timestamp).encode('utf-8') +
                    str(self.previous_hash).encode('utf-8') +
                    str(self.data).encode('utf-8'))
        return sha3.hexdigest()
