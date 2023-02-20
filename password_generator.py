import pwd_gen_utils as utils

def get_password_info():
    # Define which type of characters the password is gonna have
    print("\nSelect what characters do you want to include in the password:")
    # print("Pass the security level desired between 1 to 4 included")
    upperl = input("Uppercase Letters? (y/n): ").lower()
    lowerl = input("Lowercase Letters? (y/n): ").lower()
    nums = input("Numbers? (y/n): ").lower()
    symbols = input("Punctuation Symbols? (y/n): ").lower()
    # custom = input("Do you want to add some custom characters?")
    characters = utils.password_settings(upperl, lowerl, nums, symbols)

    # Define the length and as a final step create the password
    length = int(input("Enter the desired password length: "))
    password = utils.generate_password(length, characters)
    print(f"\n\nGenerated password: {password}\n\n")

    clipboard = input("Do you want to copy to the clipboard? (y/n): ").lower()
    if clipboard == "y":
        utils.copy_to_clipboard(password)
    
    return password

#Made by Fenner Daniel Giraldo Vargas