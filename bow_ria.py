# Q7. Bag of Words

sentences = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "the cat chased the dog"
]

# Build vocabulary
vocab = set()

for sentence in sentences:
    vocab.update(sentence.lower().split())

vocab = list(vocab)

print("Vocabulary:", vocab)
print()

# Build BoW matrix
for sentence in sentences:
    row = []
    for word in vocab:
        row.append(sentence.split().count(word))
    print(sentence)
    print(row)
    print()