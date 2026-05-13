# Q8. TF-IDF Calculation

import math

# Documents
documents = [
    "NLP is fun",
    "NLP is powerful",
    "AI and NLP are related"
]

# Vocabulary
vocab = set()

for doc in documents:
    vocab.update(doc.lower().split())

vocab = list(vocab)

# TF-IDF Calculation
for i, doc in enumerate(documents, 1):

    print("\nDocument", i, ":", doc)

    words = doc.lower().split()
    total_words = len(words)

    print("\nWord   TF      IDF      TF-IDF")
    print("-----------------------------------")

    for word in vocab:

        # TF
        tf = words.count(word) / total_words

        # IDF
        docs_with_word = 0

        for d in documents:
            if word in d.lower().split():
                docs_with_word += 1

        idf = math.log(len(documents) / docs_with_word)

        # TF-IDF
        tfidf = tf * idf

        # Print only words present in document
        if tf > 0:
            print(word,
                  round(tf, 3),
                  round(idf, 3),
                  round(tfidf, 3))