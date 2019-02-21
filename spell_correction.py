import os
import re
from collections import Counter

directory = [
    "text/court transcript",
    "text/debate-transcript",
    "text/govt-docs",
    "text/journal",
    "text/movie-script",
    "text/newspaper_newswire",
    "text/non-fiction",
    "text/technical"
]

def words(text):
    return re.findall(r'[\w0-9‘(?:’[a-zA-Z\]+)*-]+', text.lower())

words_list = []

for folder in directory:
    file_names = os.listdir(folder)
    for file_name in file_names:
        f = open(folder+'/'+file_name, 'r', encoding="utf8")
        words_list.extend(words(f.read()))

WORDS = Counter(words_list)

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    print('%s (%.10f)' % (word, (WORDS[word]+1)/(N + len(WORDS))))
    # len(WORDS) is V, V is the number of unique words
    return (WORDS[word]+1) / (N + len(WORDS)) 

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


# correction(word_input)
# for testing
# while(True):
#     word_input = input("\n\nInput word: ")
#     if word_input in WORDS:
#         print("No Error Correction")
#     else:
#         print("Most likely correction: " + correction(word_input))

# for submission
word_input = input("\n\nInput word: ")
if word_input in WORDS:
    print("No Error Correction")
else:
    print("Most likely correction: " + correction(word_input))