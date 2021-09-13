## Homework 1 - Using Python to Filter FASTA Library
import os
os.chdir('/Users/nickpaterna/Downloads/Homework/ADV-CPU') # Set working directory bc my code is stored in a GitHub repo

FASTA_file = "sequences.fasta"
raw_samples = open(FASTA_file, "r") # Opening the file defined above, contains the sequences of interest

seq_dictionary = {} # Creating a blank dictionary to build using our COVID samples
temp_key = '' # Creates a temporary key for the starting the dictionary
seq_count = 0 # An updated count of sequences collected

for line in raw_samples:
    line = line.rstrip() # Removes the 'enter' between each line in the sequence
    if line.startswith('>'):
        temp_key = line # Adds a key to the empty dictionary
        seq_dictionary[temp_key] = '' # Creates empty key without the assigned value
        seq_count += 1 # Adds to the count of the sequences
    else: # Accounting for the content after the seq-ID
       seq_dictionary[temp_key] = seq_dictionary[temp_key] + line # Adds the seq to the key identified previously - line 16

raw_samples.close() # Closes the file after script is run

seq_dictionary2 = seq_dictionary.copy() # This second dictionary represents an unfiltered copy of the one created above

has_N = 0 # Counter for the seq IDs that contain the letter N
for each in seq_dictionary2:
    if (seq_dictionary2[each].find("N") > -1): # Poses the inclusion of the letter N as a logical vector 
        has_N += 1 # Adds to the number of seqs that contain the letter N in their ID
        del(seq_dictionary[each]) # Removes the seqID that contained N from the original, retaining an unmodified copy

seq_dictionary = {value:key for key, value in seq_dictionary.items()} 
# Switch value and key so that the ID is preserved but duplicate seqs are removed
# This works bc the KEYS must always be unique but the VALUES can be changed
# In the next step we print the VALUES first bc they contain the seqID after the switch

text_file = open("COVID19_Filtered_Seq_Fall21.fasta", mode = 'w')
# For loop for filling the contents of the desired FASTA file
for key, value in seq_dictionary.items():
    text_file.write(value)
    text_file.write("\n") # Creates a space between the ID and the values assined
    text_file.write(key)
    text_file.write("\n")

print("The original FASTA cotained", seq_count, "records total.")
print("There were", (seq_count - has_N), "records without the letter N.")
print("After filtering there were", len(seq_dictionary), "unqiue records without the letter N.")
