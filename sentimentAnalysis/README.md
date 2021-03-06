# Load-JSON
Write a program that shall calculate word sentiment level, based on the user reviews from the Yelp academic dataset.
The attached file has 156,602 reviews written by Yelp members (the original dataset has 1,569,265 reviews). Each review has a text fragment and a star rating on the scale from1 (worst) to 5 (best). We assume that the words predominantly used in "bad" reviews are "bad" and the words predominantly used in "good" reviews are "good." The measure of the sentiment level of a word, therefore, is the average star rating of all reviews where the word is used.
Processing steps:

    Load the JSON data from the file and select a small subset for practicing. (The final run of the program shall include all reviews.) You must use a JSON reader.
    Extract all review texts and star ratings.
    Break each review into individual words using NLTK.
    Lemmatize the words.
    Filter out stop words and words that are not in the words corpus.
    For each lemma, calculate its average star rating. If a lemma is used in fewer than 10 reviews, discard it.
    Save the 500 most negative lemmas and 500 most positive lemmas and their respective sentiment levels in a one two-column CSV file (the lemmas in the first column, the levels in the second column), sorted in the descending order of sentiment levels.
Submit one program and one CSV file. Do not submit the original data file. You must use a CSV writer. You may not use any non-core Python modules not mentioned in the assignment (such as pandas or numpy).
Report the relative contribution of each team member (in %).
