text = """Natural Language Processing (NLP) is a field of Artificial Intelligence.
It helps computers understand human language. NLP is widely used in chatbots, translation, and speech recognition!"""

# Step 1: Split text into sentences
import re
sentences = re.split(r'[.!?]+',text)
sentences = [s.strip() for s in sentences if s.strip()]
print("Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

all_words = []
print("\nWords in each sentences:")
for i, sentence in enumerate(sentences, 1):
    words = sentence.split()
    all_words.extend(words)
    print(f"Sentence {i}:")
    print(words)

total_tokens = len(all_words)
print("\nTotal Tokens:", total_tokens)

unique_tokens = set(all_words)
print("\nUnique Tokens:", unique_tokens)

clean_text = re.sub(r'[^\w\s]', '', text)
print(clean_text)
# clean_words = clean_text.split()
# print("\nClean Words:", clean_words)
better= re.findall(r'\b\w+\b', text)
better = [s.strip() for s in better if s.strip()]
for i, better in enumerate(better, 1):
    print(f"{i}. {better}")

