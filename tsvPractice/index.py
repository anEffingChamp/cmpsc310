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
    inputFile = open('freqs.tsv', 'r')
    print(inputFile.readline())

main()
