#!/usr/bin/python3

# Write a program that shall eliminate duplicate words from a text file. The
# program shall:

# Ask the user to enter the name of an existing text file; if the file does
# not exist or cannot be opened for any other reason, the program shall print
# an error message and terminate.
# Read the content of the file and eliminate all duplicate words, except
# for the first occurrence. For the purpose of this exercise, a word is
# any sequence of characters that does not contain any spaces, and two
# words are duplicates if they differ at most in the character case (e.g.,
# "Mary" and "mArY" are duplicates).
# Write the text without duplicates into the file nodups-XXX, where
# XXX is the name of the original file. If the output file cannot be
# created, the program shall print an error message and terminate. The
# remaining words shall be written in the same order as in the
# original file (it is not enough to convert a list of words in the
# original file into a set).

# Test your program by removing duplicates from Othello. Do not write
# code for downloading the file.

import sys

targetFileName = input("Please enter the name of the target file: ")
try:
    targetFile = open(targetFileName, 'r')
except IOError:
    print ("""\nWe could not open {0}.
    - Is it present on the local file system?
    - Are its permissions properly set?\n\n""".format(targetFile))
    sys.exit()
# We have a file at this point. Now we can create the output file, and run our
# transformations.
output = 'nodups-{0}'.format(targetFileName)
try:
    output = open(output, 'w+')
except IOError:
    print ("""\nWe could not create the {0} as the target file.\n
    - Do we have write permissions to the directory?
    - Is the disk full?\n\n""".format(output))
    sys.exit()
for targetLine in targetFile:
    # TODO We could also have duplicate words across lines. What would we do
    # then?
    # TODO A duplicated would could be separated by a delimiter like
    # "word, word". How would we detect that?
    outputList = targetLine.split(' ')
    for loop in range(len(outputList) - 1, 1, -1):
        if outputList[loop] == outputList[loop - 1]:
            outputList[loop] = ''
    output.write(' '.join(outputList))
targetFile.close()
output.close()
