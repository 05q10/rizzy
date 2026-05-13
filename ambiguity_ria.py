import re

ambiguous_words = {
    "bank", "bat", "duck", "bear", "match",
    "light", "rock", "spring"
}
syntactic_patterns = {
    "with",
    "flying"
}
def detect_ambiguity(sentence):
    clean_sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    words = clean_sentence.split()
    for pattern in syntactic_patterns:
        if pattern in words or pattern in clean_sentence:
            return ("Syntactic Ambiguity",f"pattern '{pattern}' may crwate multiple sentence structures")
        
    for word in words:
        if word in ambiguous_words:
            return ("Semantic Ambiguity",f"Word '{word}' has multiple meanings")
    return ("No Ambiguity","No ambiguity detected")

sentence = input("Enter sentence: ")
atype, reason = detect_ambiguity(sentence)
print("\nSentence :", sentence)
print("Type     :", atype)
print("Reason   :", reason)