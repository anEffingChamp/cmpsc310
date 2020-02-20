"""
File freqs.tsv (attached) contains frequencies of 2,300+ words and expressions used by adolescents and young adults engaged in a certain unhealthy activity. The file has no header row. The columns are delimited by tabs. The first column of the file lists the words, the remaining columns list frequencies as floating-point numbers (some columns have missing values designated as empty strings).

Write a program that shall add another column to the table. The values in the new column shall be equal to the average (mean) value of the frequencies in each row (treat the missing values as 0). The new table shall be saved into the file freqs-mean.tsv in the same format as the original file (tab-separated, no header row, missing values designated as empty strings). Example:

Original row:

eating disorder                1.2406    1.1493    1.8994    1.3713

Processed row:

eating disorder                1.2406    1.1493    1.8994    1.3713    0.8086

You must use module csv for reading and writing the files.
"""
def main():
    inputFile  = open('freqs.tsv', 'r')
    outputFile = open('freqs-mean.tsv', 'w')
    for inputLine in inputFile:
        lineList = inputLine.split('\t')
        lineAverage = 0;
        # The last entry in a line is the new line, so we need to exclude that
        # from our calculations.
        for loop in range(1, len(lineList) - 1):
            if '' == lineList[loop]:
                lineList[loop] = 0
            lineAverage += float(lineList[loop])
        # We need to account for the first column, which is a word, not a
        # number. We also need to account for the last column, which will be the
        # uncountable new line character.
        lineAverage = str(lineAverage / (len(lineList) - 2))
        print(
            "The average frequency for " + lineList[0] + " is " + lineAverage
        )
        outputLine = inputLine + '\t' + lineAverage + '\t\n'
        outputFile.write(outputLine)

main()
