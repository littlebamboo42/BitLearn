#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

__doc__ = '''blockchain module - contains the Blockchain class

DESCRIPTION



PROPERTIES

__init__(self, identifier=0)

Parameters : NODES = config['nodes']                        list(str)
             PORT = config['port']                          str
             MAX_FILE_SIZE = 128000000                      int
             MAX_BLOCK_SIZE = config[max_block_size]        int
             INITIAL_REWARD = config[initial_reward]        int
             REWARD_HALVING = config[reward_halving]        int
             MIN_DIFFICULTY = config[minimum_difficulty]    int
Blockfile :  identifier = identifier                        int
             file_size = 0                                  int
             first_index = None                             int
             last_index = None                              int
Blockchain : difficulty = MIN_DIFFICULTY                    str
             reward = current_reward()                      int
             mempool = []                                   list(<tx01 object>)
             transactions = []                              list(dict)

METHODS

- add_block(block) :
    > return
- add_transaction(transaction) :
    > return
- calculate_merkle_root() :
    > return
- mine_block(block) : Mine new block from previous block with Proof of Work.
    > return print('Block mined')
- pick_transactions() : Select transactions with highest fee from mempool and
                        make coinbase transaction.
    > return
- size(arg) : [staticmethod] Find the byte size of an json encodable argument.
    > return size
- target(difficulty) : [staticmethod] Returns the target for a given difficulty.
    > return target

'''


import json
from sys import getsizeof

from config import *


class Blockchain(object):

    NODES = config['nodes']
    PORT = config['port']
    MAX_FILE_SIZE = 128000000
    MAX_BLOCK_SIZE = config[max_block_size]
    INITIAL_REWARD = config[initial_reward]
    REWARD_HALVING = config[reward_halving]
    MIN_DIFFICULTY = config[minimum_difficulty]

    mempool = [] #[<tx01 object>, <tx02 object>, ... , <txN object>]

    def __init__(self, identifier=0):
        #blockfile
        self.identifier = identifier #int
        self.file_size = 0 #int
        self.first_index = None #int
        self.last_index = None #int
        #blockchain
        self.difficulty = MIN_DIFFICULTY #str

    def add_block(self, block):
        if self.file_size + block.size >= MAX_FILE_SIZE:
            #Start new blockfile at new identifier
            # TODO: write first and last index in indexing file
            self.identifier = self.identifier + 1
            self.first_index = self.last_index = block.index
            with open('data/{}.dat'.format(format(self.identifier, '04x')), 'w') as f:
                f.write('[\n]')
        else:
            #Keep same file, increase last block
            self.last_index = block.index
        #Write new block
        with open('data/{}.dat'.format(format(self.identifier, '04x')), 'ab') as f:
            f.seek(-1,2)
            f.truncate()
            f.write((json.dumps(vars(block),
                                separators=(',', ':')
                                )
                     + '],\n'
                     ).encode('utf-8')
                    )
        return

    def add_transaction(self, transaction): # TODO: needs refining
        if transaction not in self.mempool and transaction.valid():
            self.mempool.append(transaction)
            return
        elif transaction in self.mempool:
            raise DoubleSpending as error
            return DoubleSpending
        else :
            return transaction.valid()

    def calculate_merkle_root(self):
        '''Calculate Merkle Tree Root using bytes of transaction hashes'''
        merkle_base = [bytes.fromhex(t['hash']) for t in self.transactions]
        while len(merkle_base) > 1:
            new_merkle_base = []
            if merkle_base % 2 == 1:
                merkle_base.append(merkle_base[-1])
            pairs = list(zip(*[iter(merkle_base)]*2)) # HACK: cuts in pairs
            for pair in pairs:
                new_merkle_base.append(sha256(b''.join(pair)).digest())
            merkle_base = new_merkle_base
        return merkle_base[0].hex() #str

    def current_reward(self, index):
        '''Calculate and returns current block reward'''
        return self.INITIAL_REWARD / 2 ** (index // self.REWARD_HALVING)

    def mine_block(self, block=None):
        '''Find the new block, with PoW.'''
        #Create genesis block
        # TODO: complete genesis block with new stuff
        if block == None:
            index = 0
            previous_hash = '0'
            transactions = 'I am the genesis block'
        #Update block header for new block
        else:
            # Initialise new block basic info
            self.size = # TODO: find and assign size of header + coinbase NOTE: updated in pick_transactions()
            index = self.last_index + 1
            self.reward = current_reward(index) #NOTE: updated in pick_transactions()
            self.pick_transactions() # NOTE: makes self.transactions, updates a bunch
            # NOTE: Should find a way to avoid rehashing
            previous_hash = sha256((str(block.size)
                                    + str(block.index)
                                    + block.previous_hash
                                    + block.merkle_root
                                    + str(block.timestamp)
                                    + block.difficulty
                                    + str(block.nonce)
                                    + str(block.number_of_transactions)
                                    + json.dumps(block.transactions)
                                    ).encode('utf-8')
                                   ).hexdigest()
            # NOTE: self.transactions built in pick_transactions()
            number_of_transactions = len(self.transactions)
            merkle_root = calculate_merkle_root()
        #Proof of work using difficulty setting
        for nonce in range(2 ** 32):
            #timestamp corresponds to the winning loop
            timestamp = int(time())
            sha = sha256((str(size)
                          + str(index)
                          + previous_hash
                          + merkle_root
                          + str(timestamp)
                          + self.difficulty
                          + str(nonce)
                          + str(number_of_transactions)
                          + json.dumps(self.transactions)
                          ).encode('utf-8')
                         ).hexdigest()
            #If under difficulty, break the previous loop and create the block
            if int(sha, 16) <= target(self.difficulty):
                print('{} - block {} mined'.format(timestamp, index))
                break
            # TODO: See if another miner has mined block
            # TODO: UTXO file
        self.mempool = list(set(self.mempool).difference(set(self.transactions)))
        add_block(Block(size,
                        index,
                        previous_hash,
                        merkle_root,
                        timestamp,
                        difficulty,
                        nonce,
                        number_of_transactions
                        json.dumps(transactions)
                        )
        return

    def pick_transactions(self):
        '''Select transactions with highest fee and make coinbase transaction'''
        self.transactions = []
        current_mempool = sorted(self.mempool,
                                 key=lambda t: vars(t)['fee'],
                                 reverse=True
                                 )
        for transaction in current_mempool:
            if self.size + transaction.size() > MAX_BLOCK_SIZE:
                break
            self.transactions.append(vars(transaction))
            self.size = self.size + transaction.size()
            self.reward = self.reward + vars(transaction)['fee']
        # Add coinbase transaction
        coinbase = Transaction('', self.reward, 0, public_key)
        coinbase.hash()
        self.transactions.insert(0, vars(coinbase))
        return

    @staticmethod
    def target(difficulty):
        '''Calculate difficulty target : target = n * 2^exp'''
        return int(difficulty[3:], 16) * 2 ** (8*(int(difficulty[:2], 16) - 3))

if __name__ == '__main__':
    pass
