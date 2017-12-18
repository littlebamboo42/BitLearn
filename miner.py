#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from datetime import datetime
from block import *
try :
    from secrets import token_bytes as random_nonce
except ImportError:
    from os import urandom as random_nonce
from hashlib import sha256

#Difficulty adjustement, number of leading 0 in hash
difficulty=3
#Nonce length adjustment in bytes
nonce_length=2

def new_block(last_block):
    '''Find the new block, with PoW'''
    #Update block header for new block
    new_index=last_block.index+1
    new_data='Hi ! I am a new block !'
    #Should find a way to avoid rehashing
    new_previous_hash=sha256(
        (
        str(last_block.index)+
        str(last_block.timestamp)+
        str(last_block.previous_hash)+
        str(last_block.nonce)+
        ).encode('utf-8')
        ).hexdigest()
    #Proof of work using difficulty setting
    while True:
        #timestamp corresponds to the winning try start
        new_timestamp=datetime.now()
        nonce=random_nonce(nonce_length)
        sha3=sha256(
            (
            str(new_index)+
            str(new_timestamp)+
            str(new_previous_hash)+
            str(nonce)+
            ).encode('utf-8')
            ).hexdigest()
        #If number of leading 0 greater or equal to difficulty setting, break
        #the previous loop and create the block
        if len(sha3)-len(sha3.lstrip('0'))>=difficulty:
            break
    return Block(new_index, new_timestamp, new_previous_hash, nonce, new_data)
