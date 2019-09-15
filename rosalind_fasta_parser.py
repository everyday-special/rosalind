#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  


def fasta_parser(filename):
	"""Given a file (filename) of a collection of DNA strings in FASTA
	format, return a dictionary of all the sqeuences where the key is
	the 4 digit sequence ID"""
	with open(filename) as f:
		sequence_list = f.read().split()
	sequence_list = ''.join(sequence_list)
	sequence_list = sequence_list.split('>Rosalind_')
	del sequence_list[0] # first item in sequence_list is an empty string
	sequence_dict = {}
	for sequence in sequence_list:
		#creates dictionary where the key is the 4 digit idetifier
		sequence_dict[sequence[:4]] = sequence[4:]
	return sequence_dict
