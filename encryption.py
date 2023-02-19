import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(master_pwd: bytes, pwd: str) -> bytes:
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
    f = Fernet(key)
    token = f.encrypt(pwd.encode())
    return token, salt

def decrypt(master_pwd: bytes, token: bytes, salt: bytes) -> str:
    try:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_pwd))
        f = Fernet(key)
        message = f.decrypt(token).decode().strip()
        return message
    except:
        os.system('cls')
        print(f"""
        {'='*35}
        Error: Master Password is not valid
        {'='*35}
        """)
        exit()