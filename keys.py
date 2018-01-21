#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

__doc__ = '''keys module - contains the KeyPair class

DESCRIPTION

Upon initation, KeyPair does all the work, by default it generates a new seed.

PROPERTIES

__init__(self, generate=True, seed=None)

seed = None                                str
private_key = self.derive_private_key()    str
public_key = self.derive_public_key()      str

METHODS

- generate_seed() : [staticmethod] Generate deterministic seed from dictionnary.
    > return str
- derive_private_key() : Derive private key from seed.
    > return str
- derive_public_key(): Derive 65 bytes hexadecimal public key from private key
                       with generator point G of SECP256K1 elliptic curve.
                       1 byte 0x04 + 32 bytes X coord + 32 bytes Y coord
    > return str

'''


try:
    from secrets import token_bytes as CSPRNG
except ImportError:
    from os import urandom as CSPRNG
try:
    from secrets import choice
except ImportError:
    from random import choice
from hashlib import sha256#, new
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from utilitybelt import int_to_charset

### INITIAL PARAMETERS
#from https://en.bitcoin.it/wiki/Private_key
#Find difference between n and Fp (2**256-2**32-2**9-2**8-2**7-2**6-2**4-1)
#n=int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141',16)


class KeyPair(object):

    '''KeyPair class to generate or derive seed and public_key'''

    def __init__(self, generate=True, seed=None):
        self.seed = seed
        #default : generate deterministic
        if generate and seed is None:
            self.seed = self.generate_seed()
            self.private_key = self.derive_private_key()
        #derive keys from seed
        elif not generate and seed is not None:
            self.private_key = self.derive_private_key()
        #deriv public_key
        self.public_key = self.derive_public_key()
        #else : error illegal move !

#        while True:
#            with open('BIP32/det_dict.txt','r') as dictionnary:
#                words = [word.strip() for word in dictionnary]
#                seed = ' '.join(choice(words) for i in range(12))
#            if int(sha256(seed.encode('utf-8')).hexdigest(),16) in range(1,n-1):
#                break
#        return seed

    @staticmethod
    def generate_seed():
        '''Generate a new deterministic seed'''
        with open('BIP32/det_dict.txt','r') as dictionnary:
            words = [word.strip() for word in dictionnary]
        return ' '.join(choice(words) for i in range(6))

    def derive_private_key(self):
        '''Derive the private key from the seed'''
        return sha256(self.seed.encode('utf-8')).hexdigest().upper()

#    def generate_private_key():
#        '''Generate a new random private key between 1 and n-1. k is hexadecimal
#        representation  of 256 random binary digits) generate using large random
#        number produced by a Cryptographically Secure Pseudo-Random
#        Number Generator (CSPRNG).'''
#        while True:
#            private_key=sha256(CSPRNG(512)).hexdigest().upper()
#            if int(private_key,16) in range(1,n-1):
#                break
#        return private_key

    def derive_public_key(self):
        '''Derive public key (K) from k using the generator point G of SECP256K1.
        K = k * G
        Find the point corresponding to k on the elliptic curve and derive the
        public key 65 bytes hexadecimal representation :
        1 byte 0x04, 32 bytes for X coordinate, 32 bytes for Y coordinate'''
        private_key_point = ec.derive_private_key(int(self.private_key,16),
                                                  ec.SECP256K1(),
                                                  default_backend())
        return private_key_point.public_key().public_numbers().encode_point().hex().upper()

#    def derive_addres(public_key):
#        #For the final base58 format
#        alphabet='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
#        #Find the RIPEMD160 (RACE Integrity Primitives Evaluation Message Digest)
#        #hash of SHA256 (Secure Hash Algorithm) hash of the public key.
#        #ripemd160 is not in the named constructors so we use new('algo', data).
#        #Create the intermediate by adding network prefix byte to the beginning.
#        #Network prefix bytes : main=b'\x00' and test=b'\x6f'.
#        prefix=b'\x00'
#        intermediate=prefix+new('ripemd160',sha256(public_key).digest()).digest()
#        #Find the checksum, the first four bytes of the double SHA256 hashing of the
#        #intermediate.
#        checksum=sha256(sha256(intermediate).digest()).digest()[:4]
#        #Find the address, the intermediate plus the checksum in bytes
#        address_bytes=intermediate+checksum
#        #Base58 conversion from integer removes the leading 0. So here they are
#        #counted to determine the number of 1 at the beginning of the address.
#        n_leading_0=len(address_bytes.hex())-len(address_bytes.hex().lstrip('0'))
#        #Find the base58 address from the number of leading 0 plus the base58 of the
#        #address bytes via integer conversion using utilitybelt.int_to_charset()
#        #opt : show the address
#        #print('A : {}'.format(address))
#        return int(n_leading_0/2)*alphabet[0]+int_to_charset(int.from_bytes(address_bytes,byteorder='big'), alphabet)'''

if __name__ == '__main__':
    pass
