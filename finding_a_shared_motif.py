#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  

from rosalind_fasta_parser import fasta_parser

sequence_dict = fasta_parser('rosalind_lcsm.txt') # parses the rosalind input file, creating a dictionary of the sequences

sequence_list = []
for seq_id in sequence_dict: # Turns the dictionary of sequences into a list of sequences
	sequence_list.append(sequence_dict[seq_id])
test_sequence = sequence_list.pop(0) # removes one sequence from the list to break into substrings

longest_sub_sequence = ''
for i in range(0, len(test_sequence)):
	for j in range(i, len(test_sequence)):
		sub_sequence = test_sequence[i:j] # searches all possible subsequences from the test sequence
		in_all_sequences = True
		for sequence in sequence_list:
			if sub_sequence not in sequence:
				in_all_sequences = False # if the subsequence is not in a DNA sequence, stop searching
				break
		if in_all_sequences == True and len(sub_sequence) >= len(longest_sub_sequence): # if the subsequence was in all DNA sequences and is the longest thus far, it is the longest shared motif
			longest_sub_sequence = sub_sequence

print(longest_sub_sequence) # print the longest shared motif
