import os
import encryption
import pwd_gen_utils as utils

def add(file_name: str, salt: bytes, token: bytes):
    if not os.path.exists("passwords"):
        os.mkdir("passwords")
    file_name = file_name + ".txt"
    with open(f"passwords/{file_name}", 'wb') as file:
        file.write(salt + b'\n')
        file.write(token)

def view(file_name: str, master_pwd: bytes):
    file_path = file_name + ".txt"
    try:
        with open(f"passwords/{file_path}", 'rb') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            salt = lines[0]
            token = lines[1]
            decrypted_pwd = encryption.decrypt(master_pwd, token, salt)
            printing(file_name, decrypted_pwd)
            if input("Do you want to copy the password to clipboard? (y/n): ").lower() == "y":
                    utils.copy_to_clipboard(decrypted_pwd)
            os.system('cls')
    except:
        not_found_error()

def delete_file(file_name):
    file_path = file_name + ".txt"
    if os.path.exists(f"passwords/{file_path}"):
        os.remove(f"passwords/{file_path}")
        print(f"{file_name} deleted successfully")
    else:
        not_found_error()

def list_files():
    files = os.listdir("passwords")
    print("\n")
    for file in files:
        file_name = file.replace(".txt", "")
        print(file_name)

def not_found_error():
    print(f"""
        {'='*35}
        Error: Account does NOT exists
        {'='*35}
        """)

def printing (name, pwd):
    print(f"""
    {'='*35}
    {name} Account
    Password: {pwd}
    {'='*35}
    """)