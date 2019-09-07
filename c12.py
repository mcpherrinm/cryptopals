#!/usr/bin/env python3

import codecs
from aes import *

# Byte-at-a-time ECB decryption (Simple)

unknown = codecs.decode(b"""
Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK""", "base64")

# encrypts buffers under ECB mode using a consistent but unknown key
# with the above data prefixed
secret = rkey()
def encrypt(data):
  return ecb_encrypt(secret, data+unknown)

encrypt(b"AAAAAAAAAA")

# Check the blocksize by encrypting increasing sizes of plaintext and verifying
# that the ciphertext increases in that increment
def check_blocksize(oracle):
  b1 = len(oracle(b""))
  sizes = set()
  for l in range(0, 3*b1):
    sizes.add(len(oracle(b"a"*l)))
  p1 = sorted(sizes)[0]
  prev = sorted(sizes)[1]
  blocksize = prev - p1
  for i in sorted(sizes)[2:]:
    diff = i - prev
    prev = i
    assert diff == blocksize
  return blocksize

blocksize = check_blocksize(encrypt)

# Verify the data looks like ECB
assert check_ecb(encrypt(b"A"*blocksize*2))

# Byte-at-a-time decryption:
# Make strings of 0 to Blocksize-1 characters and ask the oracle to encrypt.
# That makes sure every unknown byte will occur on some block boundary.
ciphertexts=[]
for shift in range(0, blocksize):
  ciphertexts.append(encrypt(b"A"*shift))

known_prefix=bytearray()

for potential in range(0, 256):
  shift = b"A"*(blocksize-1)
  ct = encrypt(shift + bytes([potential]))
  block = ct[:blocksize]
  if ciphertexts[len(shift)][:blocksize] == ct:
    print("first is ", ord(potential))
    break
