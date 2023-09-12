from Enums.Enums import SelectMode
from pyDes import ECB, CBC

class Utils():
    def __init__(self):
        self.mode = None
    
    def mode_selection(self, mode: str):
        self.mode = mode
        
        if(self.mode.lower() == SelectMode.CBC.name.lower()):
            return CBC
        elif(self.mode.lower() == SelectMode.ECB.name.lower()):
            return ECB
        else:
            raise "Please the mode you have selected does not exist"