#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from time import time
from block import *
from hashlib import sha256

#Difficulty as in bitcoin
#testing only : '1e00ffff' - 6, '1f00ffff' - 4
difficulty='1e00ffff'
target=int(difficulty[3:],16)*2**(8*(int(difficulty[:2],16)-3))
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
            str(last_block.previous_hash)+
            str(last_block.timestamp)+
            str(last_block.difficulty)+
            str(last_block.nonce)
            ).encode('utf-8')
            ).hexdigest()
        new_data='Hi ! I am a new block !'
    #Calculate reward for mining block
    reward=original_reward/2**(int(new_index/halving_blocks))
    #Proof of work using difficulty setting
    for nonce in range((2**32)-1):
        #timestamp corresponds to the winning try start
        new_timestamp=int(time())
        sha3=sha256(
            (
            str(new_index)+
            str(new_previous_hash)+
            str(new_timestamp)+
            str(difficulty)+
            str(nonce)
            ).encode('utf-8')
            ).hexdigest()
        #If number of leading 0 greater or equal to difficulty setting, break
        #the previous loop and create the block
        if int(sha3,16)<target:
            break
    return Block(new_index, new_previous_hash, new_timestamp, difficulty, nonce, new_data)
