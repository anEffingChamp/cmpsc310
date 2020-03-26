"""
Write a program that shall calculate word sentiment level, based on the user reviews from the Yelp academic dataset.
The attached file has 156,602 reviews written by Yelp members (the original dataset has 1,569,265 reviews). Each review has a text fragment and a star rating on the scale from1 (worst) to 5 (best). We assume that the words predominantly used in "bad" reviews are "bad" and the words predominantly used in "good" reviews are "good." The measure of the sentiment level of a word, therefore, is the average star rating of all reviews where the word is used.
Processing steps:

Submit one program and one CSV file. Do not submit the original data file. You must use a CSV writer. You may not use any non-core Python modules not mentioned in the assignment (such as pandas or numpy).
Report the relative contribution of each team member (in %).
"""
import csv
import json
# https://www.nltk.org/install.html
import nltk
from nltk.corpus import words
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download("wordnet")
nltk.download('words')

def main():
    # Load the JSON data from the file and select a small subset for practicing.
    # (The final run of the program shall include all reviews.) You must use a
    # JSON reader.
    with open('yelp_academic_dataset_review_small.json', 'r') as fileComplete:
        # The file comes as a single line, so we need to split it so that we can
        # parse individual JSON objects.
        reviewList   = list(fileComplete)[0].split('}, {')
        fileComplete.close()
        lemmatizer   = WordNetLemmatizer()
        lemmaWords   = {}
        # Creating a set from a list takes some time, but we do it once because
        # doing so will dramatically accelerate finding tokens and lemmas later.
        englishSet   = set(words.words('en'))
        stopWordSet  = set(stopwords.words('english'))
        ratingSorted = []
        for reviewString in reviewList:
            # TODO Our subset will be the first hundred reviews. We can remove
            # this line when we deliver the product.
            if reviewString == reviewList[100]:
                break
            # The first object will be formatted like a Python list with an
            # opening brace, so we need to remove that. We will replace it with
            # our own curly braces since we also removed the opening brace on
            # all subsequent objects.
    #   Extract all review texts and star ratings.
            review = json.loads('{' + reviewString.replace('[{', '') + '}')
    #   Break each review into individual words using NLTK.
    #   Lemmatize the words.
            reviewToken = nltk.word_tokenize(review['text'])
    #   Filter out stop words and words that are not in the words corpus.
            for word in reviewToken:
                if word.lower() in englishSet \
                and word.lower() not in stopWordSet:
                    # We lemmatize the word once we decide that it is in the
                    # English corpus, and assign it a 0 rating. We need to
                    # separately assign it an average star rating.
                    lemmas = lemmatizer.lemmatize(word.lower())
                    if lemmas not in lemmaWords:
                        # We create a list with a single key and value.
                        # The key is the count of how many times the lemma has
                        # appeared, and the value is the cumulative rating.
                        lemmaWords[lemmas] = [0, 0]
                    lemmaWords[lemmas][0] = lemmaWords[lemmas][0] + 1
                    lemmaWords[lemmas][1] = \
                        lemmaWords[lemmas][1] + int(review['stars'])
    #   For each lemma, calculate its average star rating. If a lemma is used in
    #   fewer than 10 reviews, discard it.
        for lemma in lemmaWords.items():
            if lemma[1][0] <= 10:
                continue
            ratingSorted.append([lemma[0], lemma[1][1] / lemma[1][0]])
        print(type(ratingSorted))
        ratingSorted.sort(
            key     = lambda ratingSorted: ratingSorted[1], \
            reverse = True
        )
    #   Save the 500 most negative lemmas and 500 most positive lemmas and their
    #   respective sentiment levels in a one two-column CSV file (the lemmas in
    #   the first column, the levels in the second column), sorted in the
    #   descending order of sentiment levels.
        outputFile = csv.writer(open('wordSentiment.csv', 'w'))
        for rating in ratingSorted:
            if 1001    <= len(ratingSorted) \
            and rating == ratingSorted[500]:
                break;
            print(str(rating[0]) + ': ' + str(rating[1]))
            outputFile.writerow(rating)
        if 1001 <= len(ratingSorted):
            for rating in ratingSorted[-500:]:
                print(str(rating[0]) + ': ' + str(rating[1]))
                outputFile.writerow(rating)

if __name__ == "__main__":
    main()
