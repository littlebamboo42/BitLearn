#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import time
from block import *

def create_genesis_block():
    return Block(0, time.time(), '0', 'I launched my first blockchain ! Yay !')
