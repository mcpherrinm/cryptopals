#!/usr/bin/env python3
from fn import *
from freq import *

#Single-byte XOR cipher
#The hex encoded string:
m = unhex(b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

# ... has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character
# frequency is a good metric. Evaluate each output and choose the one with the
# best score.

best = 0
bestscore = score(m)
for b in range(1, 256):
  key = [b]*len(m)
  v = score(xor(key, m))
  if v < bestscore:
    bestscore = v
    best = b

print("key:", best)
print("score:", bestscore)
print(xor([best]*len(m), m))
