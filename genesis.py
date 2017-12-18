#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from datetime import datetime
from block import *

def create_genesis_block():
    '''Create the genesis block, its hash will not respect difficulty setting'''
    index=0
    timestamp=datetime.now()
    nonce=0
    previous_hash='0'
    data='I am the genesis block'
    return Block(index, timestamp, previous_hash, nonce, data)
