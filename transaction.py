#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

__doc__ = '''transaction module - contains the Transaction class

DESCRIPTION

To create a complete transaction :
1 - initialise : tx = Transaction(input_hash, amount, fee, public_key)
2 - sign : tx.sign(private_key) # (opt) Not for coinbase
3 - hash : tx.calculate_hash()
4 - size : tx.calculate_size()

To verify a newly received transaction : received_transaction.valid()

PROPERTIES

__init__(self, input_hash, amount, fee, public_key)

Data :      input_hash = input_hash    str
            amount = amount            int
            fee = fee                  int
            pubkey = public_key        str
Signature : signature =                str
Hash :      hash =                     str

METHODS

- data() : Dump dictionnary data to string.
    > return str
- calculate_hash() : Find the hash of the signed transaction.
    * if signature is None > return UnsignedTransaction
- sign(private_key) : Sign transition using data() and private_key of sender.
    > return
- valid() : Verify if the signature can unlock the funds in the input.
    * if invalid signature > return InvalidSignature

'''

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
        return json.dumps(vars(self), separators=(',', ':'))

    def calculate_hash(self):
        self.hash = sha256(self.data().encode('utf-8')).hexdigest()
        return

    def size(self):
        self.size = getsizeof(self.data()) - 48 # NOTE: accounts for coma added in list dumps
        return

    def sign(self, private_key=None):
        self.signature = private_key.sign(self.data().encode('utf-8'),
                                          ec.ECDSA(hashes.SHA256())
                                          ).hex()
        return

    def valid(self):
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
