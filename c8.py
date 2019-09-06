#!/usr/bin/env python3

import codecs
from fn import *

for idx, line in enumerate(open("8.txt", "rb").readlines()):
  data = codecs.decode(line.strip(), "hex")
  chunks=list(chunky(data,16))

  # If a block repeats, it's probably ECB mode:
  if len(set(chunks)) != len(chunks):
    print("ECB line:", idx)

