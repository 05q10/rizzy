import nltk
nltk.download('wordnet', quiet=True)
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

words = ["running", "played", "happiness", "studies", "flies", "loving", "jumps"]

def rule_based_stem(word):
    if word.endswith('ing'):
        return word[:-3]
    if word.endswith('ed'):
        return word[:-2]
    if word.endswith('ness'):
        return word[:-4]
    if word.endswith('ies'):
        return word[:-3] + 'y'
    if word.endswith('es'):
        return word[:-2]
    if word.endswith('s'):
        return word[:-1]
    return word
print('Rule-based Stemmer:')
for word in words:
    print(word, '-->', rule_based_stem(word))
# stemmer = PorterStemmer()
# lemmatizer = WordNetLemmatizer()
# print("\nPorterStemmer vs WordNetLemmatizer:")
# print("Word          Stemmed       Lemmatized")
# for word in words:
#     print(word.ljust(14), stemmer.stem(word).ljust(14), lemmatizer.lemmatize(word))

def simple_lemma(word):
    lemma_rules = {
        'better': 'good',
        'mice': 'mouse',
        'playing': 'play',
        'jumped': 'jump',
        'walking': 'walk',
        'talked': 'talk'
    }
    return lemma_rules.get(word,word)

print("\nSimple Lemmatizer:")
for word in words:
    print(word,'-->', simple_lemma(word))