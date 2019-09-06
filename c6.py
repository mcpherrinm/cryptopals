#!/usr/bin/env python3
import codecs
from fn import *
from freq import *

## Break repeating-key XOR

# It is officially on, now.
# This challenge isn't conceptually hard, but it involves actual error-prone
# coding. The other challenges in this set are there to bring you up to speed.
# This one is there to qualify you. If you can do this one, you're probably
# just fine up to Set 6.

# There's a file [6.txt]. It's been base64'd after being encrypted with
# repeating-key XOR.

# Decrypt it.

# Here's how:

# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# Write a function to compute the edit distance/Hamming distance between two
# strings. The Hamming distance is just the number of differing bits. The
# distance between:
#    this is a test
# and
#    wokka wokka!!!
# is 37. Make sure your code agrees before you proceed.
# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
# KEYSIZE worth of bytes, and find the edit distance between them. Normalize
# this result by dividing by KEYSIZE.
# The KEYSIZE with the smallest normalized edit distance is probably the key.
# You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4
# KEYSIZE blocks instead of 2 and average the distances.
# Now that you probably know the KEYSIZE: break the ciphertext into blocks of
# KEYSIZE length.
# Now transpose the blocks: make a block that is the first byte of every block,
# and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to
# do this.
# For each block, the single-byte XOR key that produces the best looking
# histogram is the repeating-key XOR key byte for that block. Put them together
# and you have the key.
# This code is going to turn out to be surprisingly useful later on. Breaking
# repeating-key XOR ("Vigenere") statistically is obviously an academic
# exercise, a "Crypto 101" thing. But more people "know how" to break it than
# can actually break it, and a similar technique breaks something much more
# important.


test = b"this is a test"
wokka= b"wokka wokka!!!"

# Number of differing bits between two strings
def editdistance(a, b):
  return sum((bin(x ^ y).count("1") for (x, y) in zip(a, b)))
assert 37 == editdistance(test, wokka)

def transpose(data, size):
  transposed = [bytearray() for _ in range(size)]
  for chunk in chunky(data, size):
    for pos, byte in enumerate(chunk):
      transposed[pos].append(byte)
  return transposed

def keysizes(dats):
 for keysize in range(2, 43):
  chunks = chunky(dats, keysize)
  # Average edit distance over 8 chunks
  dist = 0
  for _ in range(0, 8):
      dist += (editdistance(chunks.__next__(), chunks.__next__()) / keysize)
  dist /= 8
  yield (keysize, dist)

data = codecs.decode(open("6.txt", "rb").read(), "base64")
keysize, distance = sorted(keysizes(data), key=lambda x: x[1])[0]
print(keysize, distance)

repeatingkey = bytearray()
for block in transpose(data, keysize):
  # Break single-byte xor
  best = 0
  bestscore = score(block)
  for b in range(1, 256):
    key = [b]*len(block)
    v = score(xor(key, block))
    if v < bestscore:
      best = b
      bestscore = v
  repeatingkey.append(best)

print(repeatingkey)
print(xor(repeatingkey*int(len(data)/len(repeatingkey)), data))
