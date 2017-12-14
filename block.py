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

class Block():
    def __init__(self, index, timestamp, previous_hash, data, hash_digest):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.hash = hash_digest
