from typing import Union
from Models.Encryption import DESEncrypt
from Models.Encryption import DESDecrypt
from DES.DESENCRYPTION import DESEncryption
from Utils.Utils import Utils
from Enums.Enums import TextFormat
from DTO.DTO import DTO

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
mode = Utils()
res = DTO()

# Allow requests from all origins (use with caution)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to "*" to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/encrypt")
def encrypt(item: DESEncrypt):
    # check if an item in the diction is empty or null
    empty = False

    for key,value in dict(item).items():
        
        if str(value) == "" or str(value) == None:
            if key != "iv":
                empty = True

    if empty:
        return res.response("All fields should be filled", False, "")

    selected_mode = mode.mode_selection(item.mode)

    try:
        if (len(item.secret_key) < 8 or len(item.secret_key) > 8):
            return res.response("Please the secret key should be equal 8 letters!!!", False, "")
        
        des = DESEncryption(item.secret_key, selected_mode, item.iv)
    except ValueError as err:
        return res.response("An Error Occured", False, "")

    if item.output_text.lower() == TextFormat.BASE64.name.lower():
        encryptBase64_text = des.encrypt_base64(item.text)

        return res.response("Operation Successful", True, encryptBase64_text)
    elif item.output_text.lower() == TextFormat.HEX.name.lower():
        encryptHex_text = des.encrypt_hex(item.text)

        return res.response("Operation Successful", True, encryptHex_text)
    else:
        return res.response("Select an output text", False, "")


@app.post("/decrypt")
def decrypt(item: DESDecrypt):
    # check if an item in the diction is empty or null
    empty = False

    for key,value in dict(item).items():
        
        if str(value) == "" or str(value) == None:
            if key != "iv":
                empty = True

    if empty:
        return res.response("All fields should be filled", False, "")

    selected_mode = mode.mode_selection(item.mode)
    
    try:
        if (len(item.secret_key) < 8 or len(item.secret_key) > 8):
            return res.response("Please the secret key should be equal 8 letters!!!", False, "")
        
        des = DESEncryption(item.secret_key, selected_mode, item.iv)
    except ValueError as err:
        return res.response(err, False, "")

    if item.input_text.lower() == TextFormat.BASE64.name.lower():
        decryptBase64_text = des.decrypt_base64(item.text)

        return res.response("Operation Successful", True, decryptBase64_text)
    elif item.input_text.lower() == TextFormat.HEX.name.lower():
        decryptHex_text = des.decrypt_hex(item.text)

        return res.response("Operation Successful", True, decryptHex_text)
    else:
        return res.response("Select an output text", False, "")
