"""
Solution for Counting DNA Nucleotides
This is the first problem in Project Rosalind's Bioinformatics Stronghold
"""

def count_dna_nucleotides(dna_seq):
	"""
	Counts the amount of each DNA nucleotide (A,T,C,G)
	in a given DNA sequence.
	Prints each  integer count in the order of A, C, G, T
	"""
	a_count = 0
	t_count = 0
	c_count = 0
	g_count = 0
	for dna_nuc in dna_seq.upper():
		if dna_nuc == 'A':
			a_count += 1
		elif dna_nuc == 'T':
			t_count += 1
		elif dna_nuc == 'C':
			c_count += 1
		elif dna_nuc == 'G':
			g_count += 1
	print(a_count, c_count, g_count, t_count)
	return
