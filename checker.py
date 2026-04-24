import re
import hashlib
import requests
import math

COMMON_PASSWORDS = {"123456", "password", "qwerty", "admin", "12345678"}

# ----------------------------
# BREACH CHECK (Have I Been Pwned)
# ----------------------------
def check_breach(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    hashes = response.text.splitlines()

    for h in hashes:
        hash_suffix, count = h.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0


# ----------------------------
# ENTROPY CALCULATION
# ----------------------------
def calculate_entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"[0-9]", password):
        pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool += 32

    entropy = len(password) * math.log2(pool) if pool else 0
    return round(entropy, 2)


# ----------------------------
# SMART SUGGESTIONS (NEW PART)
# ----------------------------
def generate_suggestions(password, entropy):
    suggestions = []

    # Length check
    if len(password) < 12:
        suggestions.append("Use at least 12 characters")

    # Character diversity
    if not re.search(r"[A-Z]", password):
        suggestions.append("Add uppercase letters")

    if not re.search(r"[a-z]", password):
        suggestions.append("Add lowercase letters")

    if not re.search(r"[0-9]", password):
        suggestions.append("Add numbers")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Add special characters")

    # Entropy-based advice
    if entropy < 30:
        suggestions.append("Password is very predictable — avoid common words or patterns")

    elif entropy < 60:
        suggestions.append("Good start, but increase randomness for better security")

    # Common password warning
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid common passwords used worldwide")

    return suggestions