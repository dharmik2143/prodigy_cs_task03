import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length (minimum 8 characters for strong password)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., @, $, %, &, etc.).")

    # Determine strength based on score
    if strength == 5:
        feedback.append("Strong password!")
    elif strength == 4:
        feedback.append("Good password, but can be improved.")
    elif strength == 3:
        feedback.append("Fair password, consider adding more complexity.")
    else:
        feedback.append("Weak password, please make improvements.")

    return "\n".join(feedback)

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print(result)