from enum import Enum

class SelectMode(Enum):
    ECB = 1
    CBC = 2
    
class TextFormat(Enum):
    BASE64 = 1
    HEX = 2