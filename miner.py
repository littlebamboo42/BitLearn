#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from time import time
from block import *
try :
    from secrets import token_bytes as random_nonce
except ImportError:
    from os import urandom as random_nonce
from hashlib import sha256

#Difficulty adjustement, number of leading 0 in hash
difficulty=4
#Nonce length adjustment in bytes
nonce_length=2
#Size of original reward for finding a block
original_reward=50
#Number of blocks between rewards halving
halving_blocks=2


def new_block(last_block):
    '''Find the new block, with PoW'''
    #Create genesis block
    if last_block==None:
        new_index=0
        new_previous_hash='0'
        new_data='I am the genesis block'
    #Update block header for new block
    else:
        new_index=last_block.index+1
        #Should find a way to avoid rehashing
        new_previous_hash=sha256(
            (
            str(last_block.index)+
            str(last_block.timestamp)+
            str(last_block.previous_hash)+
            str(last_block.nonce)
            ).encode('utf-8')
            ).hexdigest()
        new_data='Hi ! I am a new block !'
    #Calculate reward
    reward=original_reward/(int(new_index/halving_blocks)+1)
    print(reward)
    #Proof of work using difficulty setting
    while True:
        #timestamp corresponds to the winning try start
        new_timestamp=int(time())
        nonce=random_nonce(nonce_length)
        sha3=sha256(
            (
            str(new_index)+
            str(new_timestamp)+
            str(new_previous_hash)+
            str(nonce)
            ).encode('utf-8')
            ).hexdigest()
        #If number of leading 0 greater or equal to difficulty setting, break
        #the previous loop and create the block
        if len(sha3)-len(sha3.lstrip('0'))>=difficulty:
            break
    return Block(new_index, new_timestamp, new_previous_hash, nonce, new_data)
