#!/usr/bin/env python3

from aes import pad, unpad
from fn import hexp

# Implement PKCS#7 padding


for pads in range(5, 10):
  for l in range(0, 20):
    s = b"!" * l
    assert unpad(pad(s, pads)) == s

tests = [
  (b"", 20, b"\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14"),
  (b"YELLOW SUBMARINE", 20, b"YELLOW SUBMARINE\x04\x04\x04\x04"),
  (b"YELLOW SUBMARIN", 20, b"YELLOW SUBMARIN\x05\x05\x05\x05\x05"),
  (b"YELLOW SUBMARI", 20, b"YELLOW SUBMARI\x06\x06\x06\x06\x06\x06"),
  (b"YELLOW SUBMARINE", 8, b"YELLOW SUBMARINE\x08\x08\x08\x08\x08\x08\x08\x08"),
  (b"YELLOW SUBMARIN", 8, b"YELLOW SUBMARIN\x01"),
  (b"YELLOW SUBMARI", 8, b"YELLOW SUBMARI\x02\x02"),
  (b"YELLOW SUBMAR", 8, b"YELLOW SUBMAR\x03\x03\x03"),
  (b"YELLOW SUBMA", 8, b"YELLOW SUBMA\x04\x04\x04\x04"),
  (b"YELLOW SUBM", 8, b"YELLOW SUBM\x05\x05\x05\x05\x05"),
]

for text, blocksize, expected in tests:
  padded = pad(text, blocksize)
  print("text, padded, expected:")
  hexp(text)
  hexp(padded)
  hexp(expected)
  assert padded == expected
  assert len(padded) % blocksize == 0
  assert unpad(padded) == text
  print("")
