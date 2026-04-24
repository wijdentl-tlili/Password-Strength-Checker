from checker import check_breach, calculate_entropy, generate_suggestions

def strength_label(entropy, breach_count):
    # A breached password is always Compromised regardless of entropy
    if breach_count > 0:
        return "Compromised"
    if entropy < 40:
        return "Weak"
    elif entropy < 70:
        return "Medium"
    elif entropy < 100:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password = input("Enter your password: ")

    entropy = calculate_entropy(password)
    breach_count = check_breach(password)
    suggestions = generate_suggestions(password, entropy, breach_count)
    strength = strength_label(entropy, breach_count)

    print("\n========================")
    print(f"Entropy:  {entropy} bits")
    print(f"Strength: {strength}")

    if breach_count > 0:
        print(f"\n❌ Found {breach_count:,} times in data breaches")
    else:
        print("\n✅ Not found in known breaches")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"  • {s}")

    print("========================\n")

if __name__ == "__main__":
    main()