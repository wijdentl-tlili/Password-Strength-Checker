# 🔐 Password Strength Analyzer

A cybersecurity-focused Python tool that analyzes password security using **entropy calculation**, **real-world breach detection**, and **smart suggestions**.

---

## 🚀 Features

- 📊 **Entropy calculation** — measures real randomness in bits
- 🔥 **Breach detection** — checks against Have I Been Pwned's billion+ compromised passwords
- 🧠 **Smart suggestions** — targeted advice based on what's actually weak
- ⚠️ **Compromised override** — breached passwords are always marked Compromised, regardless of entropy score
- 🎯 **4-tier strength classification** — Weak → Medium → Strong → Very Strong

---

## 🧠 How It Works

The tool evaluates passwords across three dimensions:

**1. Entropy (bits of randomness)**  
Calculated based on character pool size and password length:
```
entropy = length × log2(pool_size)
```
| Character Set | Pool Size |
|---|---|
| Lowercase (a-z) | +26 |
| Uppercase (A-Z) | +26 |
| Digits (0-9) | +10 |
| Special characters | +32 |

**2. Strength Classification**
| Entropy | Label |
|---|---|
| < 40 bits | Weak |
| 40 – 59 bits | Medium |
| 60 – 79 bits | Strong |
| 80+ bits | Very Strong |
| Any (if breached) | Compromised |

**3. Breach Detection via k-Anonymity**  
The password is never sent to any API. Instead:
- A SHA-1 hash is computed locally
- Only the **first 5 characters** of the hash are sent to the HIBP API
- The API returns all matching hash suffixes
- The match is checked locally

This is the **k-anonymity model** — your password never leaves your machine.

---

## 📦 Installation

```bash
git clone https://github.com/wijdentl-tlili/Password-Strength-Checker.git
cd Password-Strength-Checker
pip install -r requirements.txt
```
---

## ▶️ Usage

```bash
python main.py
```

---

## 🧪 Example Outputs

**Compromised password:**
```
Enter your password: Password123!

========================
Entropy:  78.66 bits
Strength: Compromised

❌ Found 293,751 times in data breaches

Suggestions:
  • This password appeared in 293,751 data breaches — change it immediately
========================
```

**Weak password:**
```
Enter your password: 𝕳𝖊𝖑𝖑𝖔

========================
Entropy:  0 bits
Strength: Weak

✅ Not found in known breaches

Suggestions:
  • Use at least 12 characters
  • Add uppercase letters
  • Add lowercase letters
  • Add numbers
  • Add special characters
  • Password is very predictable — avoid common words or patterns
========================
```

**Strong password:**
```
Enter your password: Xy#9mPqL!2vR

========================
Entropy:  78.66 bits
Strength: Strong

✅ Not found in known breaches
========================
```

---

## 🔐 Security Design

| Concern | Solution |
|---|---|
| Password exposure | Never sent over the network — only a partial hash prefix |
| Breach database size | HIBP covers 10+ billion compromised passwords |
| Entropy accuracy | Calculated from actual character pool, not guessed from patterns |
| False sense of security | Breach status always overrides entropy-based strength label |

---

## 🛠 Tech Stack

| Library | Purpose |
|---|---|
| `requests` | HTTP calls to HIBP API |
| `hashlib` | SHA-1 hashing for k-anonymity |
| `re` | Character type detection |
| `math` | Entropy calculation |

---

## 📁 Project Structure

```
password-strength-analyzer/
├── checker.py      # Core logic: entropy, breach check, suggestions
├── main.py      
├── requirements.txt
└── README.md
```