#!/usr/bin/env python3

from aes import *
from fn import *

data = codecs.decode(open("7.txt", "rb").read(), "base64")

print(ecb_decrypt(b"YELLOW SUBMARINE", data).decode("ascii"))
