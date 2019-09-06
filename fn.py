import codecs

def unhex(a):
  return codecs.decode(a, "hex")

def hex(a):
  return codecs.encode(a, "hex")

def hexp(a):
  print(codecs.encode(a, "hex"))

def xor(a, b):
  return bytes((x ^ y for (x, y) in zip(a, b)))

# chunky
def chunky(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
