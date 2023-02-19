import utils

"""
Remember to install the pyperclip module
pip install pyperclip
"""

def main():
    print("\nWelcome to the password generator!\n")

    # Define which type of characters the password is gonna have
    print("Select what characters do you want to include in the password:")
    # print("Pass the security level desired between 1 to 4 included")
    upperl = input("Uppercase Letters? (y/n): ")
    lowerl = input("Lowercase Letters? (y/n): ")
    nums = input("Numbers? (y/n): ")
    symbols = input("Punctuation Symbols? (y/n): ")
    # custom = input("Do you want to add some custom characters?")
    characters = utils.password_settings(upperl, lowerl, nums, symbols)

    # Define the length and as a final step create the password
    length = int(input("Enter the desired password length: "))
    password = utils.generate_password(length, characters)
    print(f"\n\nGenerated password: {password}\n\n")

    clipboard = input("Do you want to copy to the clipboard? (y/n): ")
    if clipboard == "y":
        utils.copy_to_clipboard(password)

if __name__ == '__main__':
    main()

#Made by Fenner Daniel Giraldo Vargas