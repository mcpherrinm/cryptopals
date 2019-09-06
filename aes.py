from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

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
