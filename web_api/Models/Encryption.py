from pydantic import BaseModel
from typing import Union

class DESEncrypt(BaseModel):
    text: str
    mode: str
    secret_key: str
    output_text: str
    iv: Union[str, None] = None
    
class DESDecrypt(BaseModel):
    text: str
    mode: str
    secret_key: str
    input_text: str
    iv: Union[str, None] = None