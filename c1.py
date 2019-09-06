#!/usr/bin/env python3
import codecs
from fn import *

## Convert hex to base64

# The string:
hexed = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Should produce:
base64 = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n"
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

unhexed = unhex(hexed)
unbased = codecs.decode(base64, "base64")

assert unhexed == unbased

assert base64 == codecs.encode(unhexed, "base64")
assert hexed == hex(unbased)

print(codecs.encode(unhexed, "base64"))
print(base64)
