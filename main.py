from pydes import des

key = "secret_k"
text = "Hello world"
d = des()
ciphered = d.encrypt(key, text, padding=True)
plain = d.decrypt(key, ciphered, padding=True)
print("Ciphered: %r" % ciphered)
print("Deciphered: ", plain)
