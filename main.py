import os
import encryption
import file_management as myfiles
import getpass
import password_generator as passgen

#clean the console
def clear():
    os.system('cls')

#Prints menu until it gets any correct action
def menu(master_pwd):
    while True:
        clear()
        main_menu_print()
        action = input("    Your action: ").lower()

        match action:
            #Quit
            case "q":
                clear()
                exit()
            
            #View your passwords
            case "1":
                clear()
                myfiles.list_files()
                name = input("\nName of your password: ")
                myfiles.view(name, master_pwd)
                after_action_menu()
                action = input("    Your action: ").lower()
                if action == "q":
                    clear()
                    exit()
                else:
                    continue
            
            #Add a new password
            case "2":
                clear()
                name, pwd = ask_data()
                clear()
                token, salt = encryption.encrypt(master_pwd, pwd)
                myfiles.add(name, salt, token)
            #Delete a password

            case "3":
                clear()
                myfiles.list_files()
                name = input("\nName of your password: ")
                myfiles.delete_file(name)
                after_action_menu()
                action = input("    Your action: ").lower()
                if action == "q":
                    clear()
                    exit()
                else:
                    continue
            
            case _:
                clear()
                continue

def main_menu_print():
    print("""
    ==========================
    Please select any action:
    1 - View your passswords
    2 - Add a new password
    3 - Delete a password

    ----------
    q - Quit
    ==========================
    
    """)

def after_action_menu():
    print("""
    ==========================
    Please select any action:
    1 - Main menu

    ----------
    q - Quit
    ==========================

    """)

#Asks the necessary data in order to add to the txt file
def ask_data():
    name = input("\nName of your password: ")
    action = input("Do you want to create a strong random password? (y/n): ").lower()

    if action == "y":
        pwd = passgen.get_password_info()
        return name, pwd
    else:
        pwd = input("Password: ")
        return name, pwd

#Ask to write down the Master Password and also confirm it
def get_master_pwd(is_hidden: bool):
    while True:
        if is_hidden == False:
            master_pwd = input("Please, Write your master password: ")
            confirm_master_pwd = input("Please, Confirm your master password: ")
        elif is_hidden == True:
            master_pwd = getpass.getpass(prompt="Please, Write your master password: ")
            confirm_master_pwd = getpass.getpass(prompt="Please, Confirm your master password: ")
        else:
            clear()
            print("\nThe is hidden variable is not a boolean\n")
            exit()

        if master_pwd == confirm_master_pwd:
            clear()
            return master_pwd
        else:
            clear()
            continue

def main():
    #If true, You're not gonna be able to see the password you're typing, for security concerns.
    is_master_pwd_hidden = False

    clear()
    master_pwd = get_master_pwd(is_master_pwd_hidden).encode()
    menu(master_pwd)

if __name__ == '__main__':
    main()