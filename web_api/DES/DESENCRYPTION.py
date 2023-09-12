import pyDes
import base64

class DESEncryption:
    def __init__(self, key: str, mode, iv):
        self.key = key.encode('utf-8')
        self.mode = mode
        self.iv = iv.encode('utf-8') if iv else None
        self.des = pyDes.des(self.key, self.mode,self.iv, padmode=pyDes.PAD_PKCS5)

    def encrypt(self, plaintext):
        encrypted_data = self.des.encrypt(plaintext.encode('utf-8'))
        return encrypted_data

    def decrypt(self, ciphertext):
        decrypted_data = self.des.decrypt(ciphertext)
        return decrypted_data.decode('utf-8')

    def encrypt_base64(self, plaintext):
        encrypted_data = self.encrypt(plaintext)
        return base64.b64encode(encrypted_data).decode('utf-8')

    def decrypt_base64(self, base64_ciphertext):
        ciphertext = base64.b64decode(base64_ciphertext.encode('utf-8'))
        return self.decrypt(ciphertext)

    def encrypt_hex(self, plaintext):
        encrypted_data = self.encrypt(plaintext)
        return encrypted_data.hex()

    def decrypt_hex(self, hex_ciphertext):
        ciphertext = bytes.fromhex(hex_ciphertext)
        return self.decrypt(ciphertext)

