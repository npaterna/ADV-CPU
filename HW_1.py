## Homework 1 - Using Python to Filter FASTA Library

FASTA_file = "test_sequences.fasta"
raw_samples = open(FASTA_file, "r") # Opening the file defined above, contains the sequences of interest

bases = ('A', 'T', 'C', 'G')

seq_dictionary = {} # Creating a blank dictionary to build using our COVID samples
seq_names = [] # Blank list for assigning seq names
sequence = [] # Blank list for assigning sequence content

for line in raw_samples:
    if line.startswith('>'):
        seq_names.append(line[1:-1])
    elif line.startswith(bases):
        sequence.append(line)

seq_dictionary = dict(zip(seq_names, sequence))

print(seq_dictionary)
len(seq_dictionary)

raw_samples.close() # Closes the file after script is run
