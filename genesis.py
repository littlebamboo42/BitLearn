#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from datetime import datetime
from block import *
from hashlib import sha3_256

def create_genesis_block():
    index=0
    timestamp=datetime.now()
    previous_hash='0'
    data='I am the genesis block'
    sha3=sha3_256()
    sha3.update((
        str(index)+
        str(timestamp)+
        str(data)+
        str(previous_hash)
        ).encode('utf-8'))
    return Block(index, timestamp, previous_hash, data, sha3.hexdigest())
