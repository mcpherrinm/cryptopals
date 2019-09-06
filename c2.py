#!/usr/bin/env python3
from fn import *

## Fixed XOR

# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:
m1 = unhex(b"1c0111001f010100061a024b53535009181c")

# ... after hex decoding, and when XOR'd against:
m2 = unhex(b"686974207468652062756c6c277320657965")

# ... should produce:
m3 = unhex(b"746865206b696420646f6e277420706c6179")

hexp(m3)
hexp(xor(m1, m2))
assert m3 == xor(m1, m2)
