"""
Solution for Complementing a stand of DNA
This is the third problem in Project Rosalind's Bioinformatics Stronghold
"""

# tell the DNA sequence it looks pretty
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
	print(comp_dna_seq)
