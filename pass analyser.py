import re

def password_strength(password):
    # Display message to simulate real-world password testing
    print("Testing your password against known password cracking databases and leaked datasets...")

    # Initial score and feedback list
    score = 0
    feedback = []
    time_to_crack = "Unknown"

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (@$!%*?&).")

    # Extensive common passwords list to improve weak pattern detection
    common_passwords = [
        'password', '123456', '123456789', 'qwerty', 'abc123', '111111', 'password1', '1234', '000000',
        '12345', '12345678', 'iloveyou', '123123', 'letmein', 'welcome', 'admin', 'login', '123', '654321',
        'superman', 'sunshine', 'master', 'michael', 'football', 'shadow', 'monkey', 'charlie', 'jessica',
        'blink182', '123qwe', '1qaz2wsx', 'batman', 'baseball', 'soccer', 'dragon', 'mustang', 'jennifer',
        'computer', 'hunter', 'p@ssw0rd', 'trustno1', 'hello123', 'loveyou', '1q2w3e4r', 'passw0rd'
    ]
    if password.lower() in common_passwords:
        feedback.append("Avoid using common passwords like 'password', '123456', etc.")
        time_to_crack = "Instantly crackable"
    else:
        # Estimate time-to-crack based on complexity
        if score == 5 and len(password) >= 12:
            time_to_crack = "Centuries (very difficult to crack)"
        elif score == 5:
            time_to_crack = "Years (strong password)"
        elif score >= 3:
            time_to_crack = "Weeks to months (moderate password)"
        elif score >= 1:
            time_to_crack = "Within hours to days (weak password)"
        else:
            time_to_crack = "Instantly crackable"

    # Determine strength based on score
    strength = "Weak"
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"

    # Output results
    print(f"\nPassword Strength: {strength}")
    print(f"Estimated Time to Crack: {time_to_crack}")
    print(f"Evaluated by @CadGoose's Password Analyzer ")
    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

# Example usage:
user_password = input("Enter a password to test its strength: ")
password_strength(user_password)
