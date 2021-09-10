## Homework 1 - Using BioPython to Filter FASTA Library

from Bio import SeqIO # Loads in the sequencing reading functionality from biopython

filename = "test_sequences.fasta" # Identifying the file we read from
count = 0 # Initial number of seqs

### Counting the number of downloaded genomes ###
for record in SeqIO.parse(filename, "fasta"): 
    count = count + 1
print("There were " + str(count) + " records in file " + filename + " total.")

# For loop that 'parses' the records of each seq in the FASTA and adds +1 for each record found

### Number of genomes without letter 'N' ###
count = 0
for record in SeqIO.parse(filename, "fasta"):
    if 'N' not in record: 
        count = count + 1
print("There were " + str(count) + " records in file " + filename + " without letter 'N'.")

# For loop that shares the function of the previous loop BUT excludes record ID's that contain the letter N

## Number of unqiue genomes identified ##
