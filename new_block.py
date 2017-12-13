#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import time
from block import *

def new_block(last_block):
    new_index = last_block.index + 1
    new_timestamp = time.time()
    new_data = 'Hi ! I am a new block ! My index : {}'.format(new_index)
    return Block(new_index, new_timestamp, last_block.hash, new_data)
