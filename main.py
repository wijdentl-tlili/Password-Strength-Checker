from checker import check_breach, calculate_entropy, generate_suggestions

def entropy_level(entropy):
    if entropy < 30:
        return "Weak"
    elif entropy < 60:
        return "Medium"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")

    entropy = calculate_entropy(password)
    breach_count = check_breach(password)
    suggestions = generate_suggestions(password, entropy)

    print("\n========================")

    print(f"Entropy: {entropy} bits")
    print(f"Strength: {entropy_level(entropy)}")

    if breach_count > 0:
        print(f"\n❌ COMPROMISED PASSWORD")
        print(f"Found {breach_count} times in data breaches")
    else:
        print("\n✅ Not found in known breaches")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"- {s}")

    print("========================\n")

if __name__ == "__main__":
    main()