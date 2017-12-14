#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from datetime import datetime
from block import *
from os import urandom as nonce
from hashlib import sha3_256

#Difficulty adjustement, number of leading 0 in hash
difficulty=4
#Nonce length adjustment in bytes
nonce_length=2

def new_block(last_block):
    new_index=last_block.index+1
    new_timestamp=datetime.now()
    new_data='Hi ! I am a new block !'
    while True:
        sha3=sha3_256()
        sha3.update((
            str(new_index)+
            str(new_timestamp)+
            str(last_block.hash)+
            str(new_data)+
            str(nonce(nonce_length))
            ).encode('utf-8'))
        if len(sha3.hexdigest())-len(sha3.hexdigest().lstrip('0'))==difficulty:
            break
    return Block(new_index, new_timestamp, last_block.hash, new_data, sha3.hexdigest())
