#!/usr/bin/env python3
import nltk
from nltk.corpus import words
from nltk import pos_tag
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

output = dict()
tokens = nltk.pos_tag(words.words()[0:20000])
loop = 0
for token in tokens:
    if token[1] in set(['NNP', 'NNPS']):
        continue;
    print(loop)
    speechKey = token[1]
    if speechKey not in output:
        output[speechKey] = 0
    output[speechKey] = output[speechKey] + 1
    loop = loop + 1
    if loop == 10000:
        break
print(sorted(output.items())[-1])
