"""My Solution for Inferring mRNA from Protein
Problem from Project Rosalind Bioinformatics Stronghold
Returns the amount of possible mRNA sequence from a given protein sequence
modulo 1000000."""

def protein_to_mrna(protein):
	"""Returns the amount of possible mRNA sequences from a given protein
	sequence modulo 100000."""
	possible_mrnas = 1
	# RNA Codon Table
	rna_codon_dict = {
		'F' : ['UUU', 'UUC'], # Phenylalanine
		'L' : ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], # Leucine
		'S' : ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], # Serine
		'Y' : ['UAU', 'UAC'], # Tyrosine
		'Stop' : ['UAA', 'UAG', 'UGA'], # Stop codons
		'C' : ['UGU', 'UGC'], # Cysteine
		'W' : ['UGG'], # Tryptophan
		'P' : ['CCU', 'CCC', 'CCA', 'CCG'], # Proline
		'H' : ['CAU', 'CAC'], # Histidine
		'Q' : ['CAA', 'CAG'], # Glutamine
		'R' : ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], # Arginine
		'I' : ['AUU', 'AUC', 'AUA'], # Isoleucine
		'M' : ['AUG'], # Methionine
		'T' : ['ACU', 'ACC', 'ACA', 'ACG'], # Threonine
		'N' : ['AAU', 'AAC'], # Asparagine
		'K' : ['AAA', 'AAG'], # Lysine
		'V' : ['GUU', 'GUC', 'GUA', 'GUG'], # Valine
		'A' : ['GCU', 'GCC', 'GCA', 'GCG'], # Alanine
		'D' : ['GAU', 'GAC'], # Aspartic Acid
		'E' : ['GAA', 'GAG'], # Glutamic Acid
		'G' : ['GGU', 'GGC', 'GGA', 'GGG'] # Glycine
		}
		
	for amino_acid in protein.upper():
		possible_mrnas *= len(rna_codon_dict[amino_acid])
	possible_mrnas *= len(rna_codon_dict['Stop'])
	
	return possible_mrnas % 1000000
			
