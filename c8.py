#!/usr/bin/env python3

import codecs
from fn import *
from aes import *

for idx, line in enumerate(open("8.txt", "rb").readlines()):
  data = codecs.decode(line.strip(), "hex")
  if check_ecb(data):
    print("ECB line:", idx)

