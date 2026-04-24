import re
import hashlib
import requests
import math

COMMON_PASSWORDS = {"123456", "password", "qwerty", "admin", "12345678"}

def check_password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 10
        feedback.append("Increase password length (12+ recommended)")
    else:
        feedback.append("Password too short (min 8 characters)")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 15
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add numbers")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 20
    else:
        feedback.append("Add special characters")

    # Common password penalty
    if password.lower() in COMMON_PASSWORDS:
        score -= 40
        feedback.append("Avoid common passwords")

    # Clamp score
    score = max(0, min(score, 100))

    return score, feedback


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

def calculate_entropy(password):
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): pool += 32

    entropy = len(password) * math.log2(pool) if pool else 0
    return round(entropy, 2)