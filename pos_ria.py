import re
determiners  = {"the", "a", "an", "this", "that", "these", "those", "my", "your"}

conjunctions = {"and", "or", "but", "so", "yet", "nor"}

prepositions = {"in", "on", "at", "to", "for", "of",
                "with", "by", "from", "over"}

pronouns     = {"i", "he", "she", "it", "they",
                "we", "you", "me", "him", "her"}

be_verbs     = {"is", "are", "was", "were",
                "am", "be", "been", "being"}

def pos_tag(word):
    w = word.lower()
    if w in determiners:
        return "DET"
    elif w in conjunctions:
        return "CONJ"
    elif w in prepositions:
        return "PREP"
    elif w in pronouns:
        return "PRON"
    elif w in be_verbs:
        return "VERB"
    elif w.endswith("ly"):
        return "ADV"
    elif w.endswith("ing") or w.endswith("ed"):
        return "VERB"
    elif (w.endswith("tion") or
          w.endswith("ness") or
          w.endswith("ment")):
        return "NOUN"
    elif (w.endswith("ful") or
          w.endswith("ous") or
          w.endswith("ive")):
        return "ADJ"
    else:
        return "NOUN"   # Default tag
    
sentence = input("enter a sentence:")
sentence_punc = re.sub(r'[^\w\s]', '', sentence)
words = sentence.split()
print("\n{:<15} {:<10}".format("Word", "POS Tag"))
print("-" * 30)

# Tagging words
for word in sentence_punc.split():

    tag = pos_tag(word)

    print("{:<15} {:<10}".format(word, tag))
