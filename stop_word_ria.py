text = "Natural language processing is used in many applications of artificial intelligence"

stop_words = ['is', 'in', 'of', 'the', 'and', 'a', 'an', 'many']
words = text.split()
cleaned_words = []
for word in words:
    if word.lower() not in stop_words:
        cleaned_words.append(word)

cleaned_text = " ".join(cleaned_words)
print("Original Text:")
print(text) 

print("\nCleaned Text:")
print(cleaned_text)