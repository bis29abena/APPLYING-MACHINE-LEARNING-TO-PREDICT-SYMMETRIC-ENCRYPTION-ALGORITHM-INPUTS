from pydes import des
import random


def string_to_bits(s):
    """convert string to bits"""
    return ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in s])


def bytes_to_bits(bytes):
    """convert bytes to bits"""
    return ''.join(format(byte, '08b') for byte in bytes)

def generate_data(N):
    """Generate Data for training and testing"""
    d = des()
    
    key = '12345678'
    
    result = []
    
    for i in range(N):
        indata = random.getrandbits(64).to_bytes(8, "big")
        # print(indata)
        
         # getting data ready
    
        indatabits = bytes_to_bits(indata)
        # print(indatabits)
        
        outdata = d.encrypt(key=key, text=indata)
        # print(outdata)
        
        outdatabits = string_to_bits(outdata)
        # print(outdatabits)
        
        result.append((outdatabits, indatabits[0]))
        
    return result