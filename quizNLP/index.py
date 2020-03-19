#!/usr/bin/env python3
import nltk
from nltk.corpus import words
from nltk.corpus import names
nltk.download('words')
nltk.download('names')

count = 0
wordsSet = set(words.words())
for name in set(names.words()):
    if name in wordsSet:
        count = count + 1
print(count)
