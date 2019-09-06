#!/usr/bin/env python3
from fn import *
from freq import *

## Detect single-character XOR
# One of the 60-character strings in [4.txt] has been encrypted by single-character XOR.
# Find it.

d = [unhex(x) for x in open("4.txt").read().split("\n") if x != ""]

bestm = "???"
best = 0
bestscore = 100.0

for m in d:
 for b in range(1, 256):
  key = [b]*len(m)
  v = score(xor(key, m))
  if v < bestscore:
    bestscore = v
    best = b
    bestm = m

print("key:", best)
print("score:", bestscore)
print(xor([best]*len(bestm), bestm))
hexp(bestm)
