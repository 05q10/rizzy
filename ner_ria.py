# BIO Tagging based NER (without external libraries)
import re


text = "Ria lives in Mumbai and studies at IIT Bombay."


clean_text = re.sub(r'[^\w\s]', '', text)

words = clean_text.split()

locations = ["Mumbai", "Delhi", "London"]
organizations = ["IIT", "Google", "Microsoft"]

tags = []

for i, word in enumerate(words):

    # PERSON
    if word[0].isupper() and word not in locations and word not in organizations:
        if i == 0:
            tags.append((word, "B-PER"))
        else:
            tags.append((word, "I-PER"))

    # LOCATION
    elif word in locations:
        tags.append((word, "B-LOC"))

    # ORGANIZATION
    elif word in organizations:
        tags.append((word, "B-ORG"))

    # OTHER WORDS
    else:
        tags.append((word, "O"))

# Print BIO tags
for word, tag in tags:
    print(word, "->", tag)