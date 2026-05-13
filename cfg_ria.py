# -----------------------------------
# CFG Grammar Rules
# -----------------------------------

grammar = {
    "S"  : ["NP VP"],
    "NP" : ["Det N"],
    "VP" : ["V NP"],

    "Det": ["the", "a"],
    "N"  : ["cat", "dog", "boy"],
    "V"  : ["sees", "likes"]
}

# Display CFG Grammar
print("CFG Grammar Rules:\n")

for key, value in grammar.items():
    print(f"{key} -> {' | '.join(value)}")


# -----------------------------------
# CFG Vocabulary
# -----------------------------------

determiners = grammar["Det"]

nouns = grammar["N"]

verbs = grammar["V"]


# -----------------------------------
# Function to check CFG validity
# Pattern:
# Det + N + V + Det + N
# -----------------------------------

def is_valid_sentence(sentence):

    words = sentence.lower().split()

    # Sentence must contain 5 words
    if len(words) != 5:
        return False

    # CFG Pattern Check
    if (
        words[0] in determiners and
        words[1] in nouns and
        words[2] in verbs and
        words[3] in determiners and
        words[4] in nouns
    ):
        return True

    return False


# -----------------------------------
# Example Sentences
# -----------------------------------

sentences = [
    "the boy sees a dog",
    "a cat likes the boy",
    "dog sees the cat",
    "the boy running fast"
]

# -----------------------------------
# Display Results
# -----------------------------------

print("\nSentence Validation:\n")

for sentence in sentences:

    print("Sentence:", sentence)

    if is_valid_sentence(sentence):
        print("Result: VALID sentence\n")
    else:
        print("Result: INVALID sentence\n")