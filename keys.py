#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

try :
    from secrets import token_bytes as CSPRNG
except ImportError:
    from os import urandom as CSPRNG
from hashlib import sha256, new
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from utilitybelt import int_to_charset

def generate_private_key():
    '''Generate a new random private_key'''
    ### INITIAL PARAMETERS
    #Bitcoin uses SECP256K1 elliptic curve
    elliptic_curve=ec.SECP256K1()
    #from https://en.bitcoin.it/wiki/Private_key
    #Find difference between n and Fp (2**256-2**32-2**9-2**8-2**7-2**6-2**4-1)
    n=int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141',16)

    #Generate a satisfactory private key (k), between 1 and n-1. k is
    #hexadecimal representation  of 256 random binary digits) generate using
    #large random number produced by a Cryptographically Secure Pseudo-Random
    #Number Generator (CSPRNG).
    while True:
        private_key=sha256(CSPRNG(512)).hexdigest().upper()
        if int(private_key,16) in range(1,n-1):
            break
    #opt : show private key hexadecimal representation
    #print('k : {}\n'.format(private_key))

    return private_key

def derive_public_key(private_key):
    #Bitcoin uses SECP256K1 elliptic curve
    elliptic_curve=ec.SECP256K1()
    #Derive public key (K) from k using the generator point of SECP256K1 (G).
    # K = k * G
    #Find the point corresponding to k on the elliptic curve.
    private_key_point=ec.derive_private_key(int(private_key,16), elliptic_curve, default_backend())
    #Derive the public key (bytes) from the private key point.
    public_key=private_key_point.public_key().public_numbers().encode_point()
    #opt : show public key hexadecimal representation 65 bytes :
    #1 byte 0x04, 32 bytes for X coordinate, 32 bytes for Y coordinate
    #print('K : {}\n'.format(public_key.hex().upper()))
    return public_key

def derive_addres(public_key):
    #For the final base58 format
    alphabet='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    #Find the RIPEMD160 (RACE Integrity Primitives Evaluation Message Digest)
    #hash of SHA256 (Secure Hash Algorithm) hash of the public key.
    #ripemd160 is not in the named constructors so we use new('algo', data).
    #Create the intermediate by adding network prefix byte to the beginning.
    #Network prefix bytes : main=b'\x00' and test=b'\x6f'.
    prefix=b'\x00'
    intermediate=prefix+new('ripemd160',sha256(public_key).digest()).digest()
    #Find the checksum, the first four bytes of the double SHA256 hashing of the
    #intermediate.
    checksum=sha256(sha256(intermediate).digest()).digest()[:4]
    #Find the address, the intermediate plus the checksum in bytes
    address_bytes=intermediate+checksum
    #Base58 conversion from integer removes the leading 0. So here they are
    #counted to determine the number of 1 at the beginning of the address.
    n_leading_0=len(address_bytes.hex())-len(address_bytes.hex().lstrip('0'))
    #Find the base58 address from the number of leading 0 plus the base58 of the
    #address bytes via integer conversion using utilitybelt.int_to_charset()
    address=int(n_leading_0/2)*alphabet[0]+int_to_charset(int.from_bytes(address_bytes,byteorder='big'), alphabet)
    #opt : show the address
    #print('A : {}'.format(address))
    return address

def generate_key_pair():
    private_key=generate_private_key()
    public_key=derive_public_key(private_key)
    address=derive_addres(public_key)
    return (private_key, public_key.hex().upper(), address)
    #Tested against http://gobittest.appspot.com/Address

def derive_key_pair(private_key):
    public_key=derive_public_key(private_key)
    address=derive_addres(public_key)
    return (private_key, public_key.hex().upper(), address)
    
if __name__=='__main__':
    generate_key_pair()
