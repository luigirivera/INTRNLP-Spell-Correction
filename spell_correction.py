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
    return re.findall(r'\w+', text.lower())

words_list = []

for folder in directory:
    file_names = os.listdir(folder)
    for file_name in file_names:
        f = open(folder+'/'+file_name, 'r', encoding="utf8")
        words_list.extend(words(f.read()))

word_count = Counter(words_list)

print(word_count)


