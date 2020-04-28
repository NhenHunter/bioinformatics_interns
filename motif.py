#!/usr/bin/env python3
#print interation of function output
#store an item from the list in a string that as changing each iteration
#gaining access to regular expression module
import re

#call function with parameters list of split strings and kmer variable
sixmer = "TGGCGA"

#create a dictionary that contains split strings and kmer variable
with open ("og_seq.fasta", "r") as in_handle:
	sequence = in_handle.read()

#iterate through function output
seq = str(sequence)

#take last item in list of split strings, out of list
seq_list = sequence.split(sixmer)

#open file with sequence to read it , set handle
#break string at desired kmer, creating a list and save as variable
print(seq_list)

#turn variable holding read file into a collection of strings
seq_list.remove(seq_list[0])

#break string at desired kmer, creating a list and save as variable
print(seq_list)

#set variable equal to kmer 
#assign output from function to variable 
def prepend(list, str):

#print list of split strings
	str += "{0}"

#take first item in list of split strings, out of the list
	list = [str.format(i) for i in list]

#print list of split strings (sans first item)
	return (list)

#sort list of split strings without the first item
repeat_list = prepend(seq_list, sixmer)

#interpret handle and set interpretation to variable
#create function that takes in two parameters
for item in repeat_list:

#the two parameters take in two different collections
	print(item)

#retreive list from function
