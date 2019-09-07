#!/usr/bin/env python3

import os
from collections import Counter
from aes import *
from fn import *

## An ECB/CBC detection oracle
# Now that you have ECB and CBC working:

# Write a function that encrypts data under an unknown key --- that is, a
# function that generates a random key and encrypts under it.
# The function should look like:
# encryption_oracle(your-input)
# => [MEANINGLESS JIBBER JABBER]
# Under the hood, have the function append 5-10 bytes (count chosen randomly)
# before the plaintext and 5-10 bytes after the plaintext.  Now, have the
# function choose to encrypt under ECB 1/2 the time, and under CBC the other
# half (just use random IVs each time for CBC). Use rand(2) to decide which to
# use.

def encryption_oracle(data):
  key = rkey()

  # append & prepend data...
  before = os.urandom(ord(os.urandom(1)) % 5 + 5)
  after = os.urandom(ord(os.urandom(1)) % 5 + 5)

  data = before + data + after

  if ord(os.urandom(1)) > 128:
    return "ecb", ecb_encrypt(key, data)
  else:
    iv=os.urandom(16)
    return "cbc", cbc_encrypt(key, iv, data)


# Detect the block cipher mode the function is using each time. You should end
# up with a piece of code that, pointed at a block box that might be encrypting
# ECB or CBC, tells you which one is happening.

def detect():
  # put a couple blocks of plaintext
  testdata = b"a" * 64

  spoiler, ct = encryption_oracle(testdata)

  # ECB has duplicate blocks
  if check_ecb(bytes(ct)):
    assert spoiler == "ecb"
    print("correctly guessed ecb")
  else:
    assert spoiler == "cbc"
    print("correctly guessed cbc")

for _ in range(0, 10):
  detect()
