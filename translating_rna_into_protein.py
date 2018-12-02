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
	
def rna_to_protein(rna_seq, rna_codon_dict):
	"""returns the protein sequence for a given RNA sequence"""
	protein_sequence = ''
	counter = 0
	while counter < len(rna_seq):
		codon = rna_seq[counter : counter + 3]
		if codon in rna_codon_dict['Stop']:
			break
		for amino_acid in rna_codon_dict:
			if codon in rna_codon_dict[amino_acid]:
				protein_sequence += amino_acid
		counter += 3
	return protein_sequence
