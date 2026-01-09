# Simple Password Generator

import random
import string

print("--- SIMPLE PASSWORD GENERATOR ---\n")

try:
    length = int(input("Enter password length (minimum 6): "))
    if length < 6:
        print("Password length should be at least 6 ❌")
        exit()
except ValueError:
    print("Invalid input! Enter a number ❌")
    exit()

characters = string.ascii_letters + string.digits + "!@#$%^&*()"
password = "".join(random.choice(characters) for _ in range(length))

print(f"\nYour generated password: {password}")
print("Keep it safe! 🔒")