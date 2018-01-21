#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

__doc__ = '''contains the Transaction class

* To create a complete transaction :
1 - initialise : tx = Transaction(input_hash, amount, fee, public_key)
2 - (opt) sign : tx.sign(private_key) (not for coinbase transaction)
3 - hash : tx.calculate_hash()
4 - size : tx.calculate_size()

* To verify a newly received transaction : received_transaction.valid()

'''

#PROPERTIES

#Data :      input_hash = input_hash    str
#            amount = amount            int
#            fee = fee                  int
#            pubkey = public_key        str
#Signature : signature =                str
#Hash :      hash =                     str

import json
from sys import getsizeof
from hashlib import sha256
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class Transaction(object):

    def __init__(self, input_hash, amount, fee, destination, private_key):
        #Data
        self.input_hash = input_hash #str hexa
        self.amount = amount #int
        self.fee = fee #int
        self.pubkey = destination #str
        return

    def data(self):
        '''Returns json formatted string of the class dictionnary.
        The transaction is be stored in this format in the blocks.'''
        return json.dumps(vars(self), separators=(',', ':'))

    def calculate_hash(self):
        '''Find the hash of the transaction using .data().'''
        self.hash = sha256(self.data().encode('utf-8')).hexdigest()
        return

    def size(self):
        '''Returns the size in bytes of the transition .data()'''
        return getsizeof(self.data()) - 49

    def sign(self, private_key=None):
        '''Sign transition using data() and private_key of sender.'''
        self.signature = private_key.sign(self.data().encode('utf-8'),
                                          ec.ECDSA(hashes.SHA256())
                                          ).hex()
        return

    def valid(self): # TODO: validate against UTXO pubkey not this tx pubkey
        '''Verify if the signature can unlock the funds in the input. Returns
        True if signature matches pubkey. If not, returns InvalidSignature.'''
        try:
            self.pubkey.verify(bytes.fromhex(self.signature),
                               self.data().encode('utf-8'),
                               ec.ECDSA(hashes.SHA256())
                               )
            return True
        except InvalidSignature as error:
            return error

if __name__ == '__main__':
    pass
