import random

# Training text
text = """
I love NLP
I love machine learning
machine learning is fun
NLP is fun
"""
    
# -----------------------------------
# Step 1: Tokenize text
# -----------------------------------

words = text.lower().split()

# -----------------------------------
# Step 2: Create bigrams
# -----------------------------------

bigrams = {}

for i in range(len(words) - 1):

    current_word = words[i]
    next_word = words[i + 1]

    # Create dictionary entry
    if current_word not in bigrams:
        bigrams[current_word] = []

    bigrams[current_word].append(next_word)

# -----------------------------------
# Display Bigram Model
# -----------------------------------

print("Bigram Dictionary:\n")

for word in bigrams:
    print(word, "->", bigrams[word])

# -----------------------------------
# Step 3: Generate Text
# -----------------------------------

current_word = "i"

generated_text = [current_word]

# Generate next 10 words
for _ in range(10):

    # Stop if no next word exists
    if current_word not in bigrams:
        break

    # Randomly choose next word
    next_word = random.choice(bigrams[current_word])

    generated_text.append(next_word)

    # Move forward
    current_word = next_word

# -----------------------------------
# Display Generated Text
# -----------------------------------

print("\nGenerated Text:\n")
print(" ".join(generated_text))