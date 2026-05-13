# Prior probabilities
P_spam = 0.6
P_ham = 0.4

# Word probabilities
spam_probs = {
    "free": 0.5,
    "win": 0.4,
    "money": 0.3
}

ham_probs = {
    "free": 0.1,
    "win": 0.05,
    "money": 0.1
}

# Test sentence
sentence = "free win money"

words = sentence.split()

# -----------------------------
# Compute Spam Probability
# -----------------------------
spam_score = P_spam

for word in words:
    spam_score *= spam_probs[word]

# -----------------------------
# Compute Ham Probability
# -----------------------------
ham_score = P_ham

for word in words:
    ham_score *= ham_probs[word]

# -----------------------------
# Display Results
# -----------------------------
print("Spam Score =", spam_score)
print("Ham Score =", ham_score)

# Classification
if spam_score > ham_score:
    print("\nSentence is classified as: SPAM")
else:
    print("\nSentence is classified as: HAM")