import re

# Input text
text = "Hello World! NLP 2025 is AMAZING!!! Python3 is fun."

print("Original Text:")
print(text)

text = text.lower()

text = re.sub(r'\d+', '', text)

text = re.sub(r'[^\w\s]', '', text)


text = re.sub(r'\s+', ' ', text).strip()


print("\nCleaned Text:")
print(text)