from checker import check_password_strength, check_breach, calculate_entropy

def display_strength(score):
    if score < 40:
        return "Weak"
    elif score < 70:
        return "Medium"
    else:
        return "Strong"
    
def entropy_level(entropy):
    if entropy < 30:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)
    breach_count = check_breach(password)
    entropy = calculate_entropy(password)

    print(f"\nScore: {score}/100")
    print(f"Entropy: {entropy}")
    print(f"Entropy Level: {entropy_level(entropy)}")

    if breach_count:
        print(f"⚠️ This password was found {breach_count} times in data breaches!")
    else:
        print("✅ This password was NOT found in known breaches")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()