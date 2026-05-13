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

# import re

# email = "test@gmail.com"
# phone = "(123) 456-7890"

# email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# phone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'

# if re.match(email_pattern, email):
#     print("Valid Email")

# if re.match(phone_pattern, phone):
#     print("Valid US Phone Number")

# Regex (Regular Expression)

# - Regex is a pattern matching technique used for searching, extracting, and cleaning text.

# Python module:
# import re

# Important functions:
# - re.search()   -> checks pattern anywhere in text
# - re.match()    -> checks pattern at the start
# - re.findall()  -> returns all matches
# - re.sub()      -> replace/remove pattern
# - re.split()    -> split text using pattern

# Important symbols:
# - \d  -> digit
# - \w  -> word character
# - \s  -> whitespace
# - .   -> any character
# - *   -> zero or more
# - +   -> one or more
# - ?   -> zero or one
# - ^   -> start of string
# - $   -> end of string
# - ()  -> group
# - |   -> OR
# - [ ] -> character class
# - [^ ]-> negation

# Common patterns:
# - Name:  \b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b
# - Email: \b[\w\.-]+@[\w\.-]+\.\w+\b
# - Indian mobile: (?:\+91[-\s]?)?[6-9]\d{9}
# - US mobile: (\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})
# - Date: \b\d{2}/\d{2}/\d{4}\b

# Limitations:
# - Regex is pattern-based, not context-based.
# - Good for structured text.
# - Not enough for full semantic understanding.