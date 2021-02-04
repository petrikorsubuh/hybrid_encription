from Crypto.Cipher import AES
import pyscrypt, os, binascii
import array

def encrypt_AES_GCM(msg, password):
  kdfSalt = os.urandom(16)
  secretKey = pyscrypt.hash(password, kdfSalt, 1024, 8, 1, 32) # slower but more correct by 16384
  aesCipher = AES.new(secretKey, AES.MODE_GCM)
  ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
  return ciphertext

def decrypt_AES_GCM(encryptedMsg, password):
  (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
  secretKey = pyscrypt.hash(password, kdfSalt, 1024, 8, 1, 32) # slower but more correct by 16384
  aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
  plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
  return plaintext

# #msg = b'Message for AES-256-GCM + Scrypt encryption'
# msg = input("masukan pesan aes:").encode()
# password =  input("masukan key aes:").encode()
#
# encryptedMsg = encrypt_AES_GCM(msg, password)
# print("encryptedMsg", {
# 'kdfSalt': binascii.hexlify(encryptedMsg[0]),
# 'ciphertext': binascii.hexlify(encryptedMsg[1]),
# 'aesIV': binascii.hexlify(encryptedMsg[2]),
# 'authTag': binascii.hexlify(encryptedMsg[3])
# })
#
# decryptedMsg = decrypt_AES_GCM(encryptedMsg, password)
# print("decryptedMsg", decryptedMsg)
