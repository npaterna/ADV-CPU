## Homework 1 - Using Python to Filter FASTA Library

FASTA_file = "sequences.txt"
raw_samples = open(FASTA_file, "r") # Opening the file defined above, contains the sequences of interest

seq_dictionary = {} # Creating a blank dictionary to build using our COVID samples
for item in raw_samples:
    (key, value) = item.split(sep = '>')
    seq_dictionary[key] = value

print(seq_dictionary)
#raw_samples.close
