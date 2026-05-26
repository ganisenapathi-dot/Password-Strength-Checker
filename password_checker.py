import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search("[A-Z]", password):
        strength += 1

    if re.search("[a-z]", password):
        strength += 1

    if re.search("[0-9]", password):
        strength += 1

    if re.search("[@#$%^&*!]", password):
        strength += 1

    if strength <= 2:
        return "Weak Password"
    elif strength <= 4:
        return "Medium Password"
    else:
        return "Strong Password"

password = input("Enter Password: ")
print("Password Strength:", check_password_strength(password))