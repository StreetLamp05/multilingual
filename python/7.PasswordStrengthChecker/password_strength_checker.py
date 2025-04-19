"""
Input a password
- [x] Check for length, numbers, uppercase/lowercase, symbols
- [x] Use string methods or `re` (regex) module
"""

import re # regex module

"""
From: https://support.microsoft.com/en-us/windows/create-and-use-strong-passwords-c5cebb49-8c53-4f5e-2bc4-fe357ca048eb
 Atleast 12 characters
 contains:
 uppercase letters
 lowercase letters
 numbers
 symbols
 
 not a word from the dictonary (but idk how to do that with regex... so i'll omit this requirement..."
 
 using:
 https://regex101.com/ to test
 got:
 "^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[!@#$%^&*()_+]).{12,}$"
"""

def main():
    pass_strong = False
    while not pass_strong:
        test = input("Enter a password: ")
        if is_strong(test):
            pass_strong = True
            print("Inputted password is strong")
        else:
            print("Weak password, strong passwords should be > 12 characters long, and contain a combination "
                  "of upper case, lowercase letters, numbers, and symbols.")

def is_strong(password:str) -> bool:
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+]).{12,}$'
    return bool(re.match(pattern, password))


if __name__ == "__main__":
    main()
