#!/usr/bin/env python3
"""
Shakespeare's plays traditionally have many words that are now either out of use
or spelled differently. Write a program that displays the 25 most frequently
used alphabetic words in Othello that are not in the corpus of the modern
English words (the NLTK words).

Your program shall download (and cache, and read from the cache, if available)
the file with urllib. The program then shall extract the text with
BeautifulSoup, tokenize the text with NLTK, lemmatize the words, and count the
words that are not in the words corpus. Remember that the words in the corpus
are in the lower case.

reference:
http://shakespeare.mit.edu/othello/full.html
"""
import sys
import urllib.request
import nltk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
nltk.download("wordnet")
nltk.download('words')

def main():
    # Your program shall download (and cache, and read from the cache, if
    # available) the file with urllib.
    try: fileOutput = open('othello.html', 'r')
    except:
        fileOutput = open('othello.html', 'w')
        fileOutput.writelines(
            str(urllib.request.urlopen(
                'http://shakespeare.mit.edu/othello/full.html'
            ).read())
        )
    input = BeautifulSoup(fileOutput, 'html.parser')
    # The program then shall extract the text with
    # BeautifulSoup, tokenize the text with NLTK, lemmatize the words, and count
    # the words that are not in the words corpus. Remember that the words in
    # the corpus
    englishSet = set(words.words('en'))
    for element in input.find_all('blockquote'):
        # We seem to pick up a number of new lines in these words, so lets just
        # replace them all with empty string.
        quoteToken = nltk.word_tokenize(element.get_text().replace('\\n', ''))
        print(quoteToken)

main()