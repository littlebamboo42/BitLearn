#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import hashlib

print('Guaranteed:\n{}'.format(
', '.join(sorted(hashlib.algorithms_guaranteed))))

print('Available:\n{}'.format(
', '.join(sorted(hashlib.algorithms_available))))
