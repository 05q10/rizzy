import re

# Input text
text = "Hello World! NLP 2025 is AMAZING!!! Python3 is fun."

print("Original Text:")
print(text)

# -----------------------------------
# Step 1: Convert to lowercase
# -----------------------------------

text = text.lower()

# -----------------------------------
# Step 2: Remove numbers
# -----------------------------------

text = re.sub(r'\d+', '', text)

# -----------------------------------
# Step 3: Remove punctuation
# -----------------------------------

text = re.sub(r'[^\w\s]', '', text)

# -----------------------------------
# Step 4: Remove extra spaces
# -----------------------------------

text = re.sub(r'\s+', ' ', text).strip()

# -----------------------------------
# Display Cleaned Text
# -----------------------------------

print("\nCleaned Text:")
print(text)