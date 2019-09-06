#!/usr/bin/env python3

import codecs
from aes import *
import os

data = codecs.decode(open("10.txt", "rb").read(), "base64")

iv=b"\x00"*16
print(cbc_decrypt(b"YELLOW SUBMARINE", iv, data).decode("ascii"))

key=os.urandom(16)
iv=os.urandom(16)

msg = b"hello there world"
assert msg == cbc_decrypt(key, iv, cbc_encrypt(key, iv, msg))
