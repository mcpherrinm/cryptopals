from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from collections import Counter

from fn import *

backend = default_backend()

# the base aes128 block function
def aes_encrypt_block(key, data):
  assert(len(key) == 16)
  assert(len(data) == 16)

  cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
  c = cipher.encryptor()
  return c.update(data) + c.finalize()

def aes_decrypt_block(key, data):
  assert(len(key) == 16)
  assert(len(data) == 16)

  cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
  d = cipher.decryptor()
  return d.update(data) + d.finalize()

# PKCS#7 padding
def pad(data, blocksize):
  missing = blocksize - (len(data) % blocksize)

  data = bytearray(data)
  for _ in range(missing):
    data.append(missing)
  return data

def unpad(data):
  last = data[-1]
  # padding should be all the same byte:
  assert len((set(data[-last:]))) == 1
  return data[:-last]

def ecb_encrypt(key, data):
  ret = bytearray()
  for chunk in chunky(pad(data, 16), 16):
    ret += aes_encrypt_block(key, chunk)
  return ret

def ecb_decrypt(key, data):
  ret = bytearray()
  for chunk in chunky(data, 16):
    ret += aes_decrypt_block(key, chunk)
  return unpad(ret)

def cbc_encrypt(key, iv, data):
  ret = bytearray()
  for chunk in chunky(pad(data, 16), 16):
    ct = aes_encrypt_block(key, xor(chunk, iv))
    iv = ct
    ret += ct
  return ret

def cbc_decrypt(key, iv, data):
  ret = bytearray()
  for chunk in chunky(data, 16):
    plain = xor(iv,aes_decrypt_block(key, chunk))
    iv = chunk
    ret += plain
  return unpad(ret)

# If a block repeats, it's probably ECB mode:
def check_ecb(data):
  chunks=list(chunky(data,16))
  c = Counter(chunks)
  for f in c:
    if c[f] > 1:
      return True
  return False

