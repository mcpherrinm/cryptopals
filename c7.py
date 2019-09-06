#!/usr/bin/env python3

from aes import *
from fn import *

data = codecs.decode(open("7.txt", "rb").read(), "base64")

# ECB is just repeatedly applying the AES block function
for chunk in chunky(data, 16):
  print(aes_decrypt_block(b"YELLOW SUBMARINE", chunk).decode("ascii"), end="")
