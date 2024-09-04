import re

def check_password_strength(password):
    # Initialize strength variables
    length = len(password)
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess the strength based on criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Provide feedback based on the strength score
    if strength == 5:
        feedback = "Very Strong"
    elif strength == 4:
        feedback = "Strong"
    elif strength == 3:
        feedback = "Moderate"
    elif strength == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    return {
        'strength_score': strength,
        'feedback': feedback,
        'length_ok': length >= 8,
        'has_upper': has_upper,
        'has_lower': has_lower,
        'has_digit': has_digit,
        'has_special': has_special
    }

# Example Usage
password = input("Enter your password: ")
result = check_password_strength(password)

print("\nPassword Strength Assessment")
print(f"Strength Score: {result['strength_score']}/5")
print(f"Feedback: {result['feedback']}")
print(f"Meets Length Requirement (>= 8): {result['length_ok']}")
print(f"Contains Uppercase Letters: {result['has_upper']}")
print(f"Contains Lowercase Letters: {result['has_lower']}")
print(f"Contains Digits: {result['has_digit']}")
print(f"Contains Special Characters: {result['has_special']}")
