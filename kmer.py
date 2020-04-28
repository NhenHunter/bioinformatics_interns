#!/usr/bin/env python3
from collections import Counter
from collections import OrderedDict

def get_all_k_mer(string, k=1):
   length = len(string)
   return [string[i: i+ k] for i in range(length-k+1)]

with open ("/Users/nhenhunter/rosalind/og_seq.fasta", "r") as in_handle:
	string = in_handle.read().replace('\n', '')

print(string)
kmer_dict = Counter(get_all_k_mer(string, k=6))


print(kmer_dict)




#obtain list output from function
#import modules 
#find the length of the sequence
#open a file to read, replace linefeed with space
#create a dictionary using a module
#call function and provide string and kmer length as parameters
#print dictionary
#create a list that searches for sets of similar nucleotides by "stepping" through a sequence and recording each of parameter length with corresponding base pairs
#create function that takes two parameters
