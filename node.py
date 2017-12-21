#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from miner import *
from generate_key_pair import *
import json
import os
from time import time

wallet=generate_key_pair()
print('k : {}\nA : {}'.format(wallet[0], wallet[2]))

#blockchain.dat folder
location='data/'

previous_block=None

for identifier in range(int('ffff',16)):
    blk_file='{}blk{}.dat'.format(location, format(identifier,'04x'))

    try:
        os.remove(blk_file)
    except:
        pass

    with open(blk_file,'a') as blk:
        start=int(time())
        blk.write('[\n')

    #Create and lengthen the blockchain
    for i in range(128):
        block_to_add = new_block(previous_block)
        with open(blk_file,'a') as blk:
            json.dump(vars(block_to_add), blk, indent=2)
            blk.write(',\n')
        previous_block = block_to_add

    with open(blk_file,'a') as blk:
        blk.write(str(int(time()-start)))
        blk.write(']')
