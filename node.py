#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import sys
import urllib
from time import time
from flask import Flask,request,json

from block import *
from blockchain import *
from config import *
from keys import *
from transaction import *

node=Flask(__name__)

################################################################################
#PARAMETERS

NODE_TYPE = config['type']
NODE_MINER = config['miner']

#data storage folder
DATA_DIR = config['data_dir']
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

"""#Get other nodes IP address
with open('nodes.txt','r') as nodes_file :
    nodes=list(map(lambda node: node.strip(), (node for node in nodes_file)))
#print(nodes)"""

#Get blockchain info from other nodes
last_index = 0
previous_block = None
identifier = 0
for node in nodes:
    url='http://{}:{}/find_blockchain'.format(node,port)
    try:
        blockchain_info = urllib.request.urlopen(url).read()
        if blockchain_info[0] >= last_index:
            last_index = blockchain_info[0]
        if blockchain_info[1] >= identifier:
            identifier = blockchain_info[1]
    except:
        pass

#Difficulty as in bitcoin min : 1d00ffff - 8 leading 0
#testing only : '1e00ffff' - 6 leading 0, '1f00ffff' - 4 leading 0
difficulty = '1e00ffff'

################################################################################
#NODE

#Start node with new or old keys
if input('Generate new keys ? (y/n) ').lower() == 'n':
    seed = input('Seed : ').lower()
    keys = KeyPair(False, seed)
    print('Pubkey :',keys.public_key)
else:
    keys = KeyPair()
    print('Seed : {}\nPubkey : {}'.format(keys.seed, keys.public_key))
"""
@node.route('find_blockchain')
def find_blockchain():
    '''Returns blockchain index and identifier to requesting node'''
    return #[blockchain_index,identifier]

#When new block, append blockchain, edit mempool, edit UTXO, send block again
@node.route('/new_block', methods=['POST'])
def add_new_block():
    '''Append the blockchain with new block if it is valid'''
    global blk_dir
    global identifier
    if request.method == 'POST':
        block_to_add_dict=request.get_json()
    blk_file='{}blk{}.dat'.format(blk_dir, format(identifier,'05x'))
    #Make new blk_file if the max size is reached
    try:
        if os.path.getsize(blk_file)+sys.getsizeof(json.dumps(block_to_add_dict))>=128000000:
            identifier+=1
            blk_file='{}blk{}.dat'.format(blk_dir, format(identifier,'05x'))
            ##LATER : Modify indexing file : blk*****.dat contains blocks m to n
    except OSError:
        pass
        #File doesnt exist, create it
    #Append block to blk_file
    '''
    if new_block.index>last_index and verify_block(block_to_add,difficulty_target)==True:
        with open(blk_file,'a') as blk:
            json.dump(block_to_add_dict,blk)
            blk.write(',\n')
        return 'block accepted'
    else: return 'block rejected'
    '''
    ##LATER : elif same index : competing blocks, wait

################################################################################
#MINING

#If the node is a miner, then start mining
from miner import *
while miner_node==True:
    #Select transactions from mempool
    #Create Coinbase
    #Create Merkle Tree
    #Mine block block_to_add = mine_new_block(last_block,difficulty_target)
    #Send block
    '''
req = urllib.Request('http://example.com/api/posts/create')
req.add_header('Content-Type', 'application/json')

response = urllib.urlopen(req, json.dumps(vars(block_to_add))
'''

################################################################################
#OLD MINING
'''
for identifier in range(int('ffff',16)):
    blk_file='{}blk{}.dat'.format(blk_dir, format(identifier,'05x'))

    try:
        os.remove(blk_file)
    except:
        pass

    with open(blk_file,'a') as blk:
        start=int(time())
        blk.write('[\n')

    #Create and lengthen the blockchain
    for i in range(128):
        block_to_add = mine_new_block(previous_block)
        with open(blk_file,'a') as blk:
            json.dumps(vars(block_to_add))
            blk.write(',\n')
        previous_block = block_to_add

    with open(blk_file,'a') as blk:
        blk.write(str(int(time()-start)))
        blk.write(']')
'''
"""
