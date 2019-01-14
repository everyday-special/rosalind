"""
Solution for Locating Restriction Sites
From Project Rosalind's Bioinformatics Stronghold
Assumes the FASTA formatting is in the form of '>Rosalind_####' 
Just run reverse_palindrome(filename) with filename being the filename
as a string.
"""

def extract_sequence_from_file(filename):
	"""opens file and extracts the DNA sequence"""
	with open(filename) as f:
		sequence = f.read().split()
	sequence = ''.join(sequence)
	sequence = sequence[14:]
	return sequence

def reverse_palindrome(filename):
	"""Finds reverse palindromes 4 to 12 nucleotides in length and
	and prints the position + 1 (so that the first position is 1 not 0)
	and the length of the reverse palindrome"""
	dna_sequence = extract_sequence_from_file(filename)
	site_dict = {}
	for i in range(len(dna_sequence.upper())):
		for n in range(2, 7):
			if complement_dna(dna_sequence[i:i + n]) == dna_sequence[i + n:i + 2 * n] and (i + 2 * n) <= len(dna_sequence):
				site_dict[i + 1] = n * 2
	for site in site_dict:
		print(site, site_dict[site])

def complement_dna(dna_seq):
	"""Generate a complementary strand of DNA"""
	comp_dna_seq = ''
	for dna_nuc in dna_seq.upper():
		if dna_nuc == 'A':
			comp_dna_seq = 'T' + comp_dna_seq
		elif dna_nuc == 'T':
			comp_dna_seq = 'A' + comp_dna_seq
		elif dna_nuc == 'C':
			comp_dna_seq = 'G' + comp_dna_seq
		elif dna_nuc == 'G':
			comp_dna_seq = 'C' + comp_dna_seq
	return comp_dna_seq
