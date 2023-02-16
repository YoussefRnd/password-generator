"""password generator"""
import random
import string


def password_generator(length):
    """Generates a password of the specified length."""
    print(
        """Choose the type of password you want to generate: 
            1. Characters
            2. Numbers
            3. Symbols
            4. Exit"""
    )
    password_type = ""
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            password_type += string.ascii_letters
        elif choice == 2:
            password_type += string.digits
        elif choice == 3:
            password_type += string.punctuation
        elif choice == 4:
            break
        else:
            print("Invalid choice entered. Please try again.")
    password = []
    for _ in range(length):
        password.append(random.choice(password_type))
    print("Your password is " + "".join(password))


password_generator(int(input("Enter the length of the password: ")))
