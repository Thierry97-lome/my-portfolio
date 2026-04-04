def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+" for c in password):
        score += 1

    return score

password = input("Enter a password to check: ")
strength = check_password(password)

levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
print("Password Strength:", levels[strength])
