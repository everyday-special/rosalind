"""Solution to RNA Splicing
From Project Rosalind Bioinformatics Stronghold.
Given a file of DNA sequence strings in FASTA Format where the first 
seuqence is a string of at most 1 kbp and the rest are a collection of
substrings acting as intron sequences. Prints the protein sequence of
the first DNA sequence with the exons spliced out.
Run splice_transcribe_translate(filename) to get the solution."""

def extract_sequences(filename):
	"""Extracts the sequences from the file. The RNA sequence containing
	introns and exons has the key 'rna_sequence' while the introns have
	the 4 digit sequence ID"""
	with open(filename) as f:
		# convert file contents into dictionary of 4 digit sequence id and sequence
		sequence_list = f.read().split()
	sequence_list = ''.join(sequence_list)
	sequence_list = sequence_list.split('>Rosalind_')
	dna_sequence = sequence_list[1][4:]
	del sequence_list[1]
	del sequence_list[0] # first item in sequence_list is an empty string
	sequence_dict = {}
	sequence_dict['dna_sequence'] = dna_sequence
	for sequence in sequence_list:
		# creates a dictionary of 
		sequence_dict[sequence[:4]] = sequence[4:]
		seq_id = sequence[:4]
	return sequence_dict
	
def remove_introns(filename):
	"""Removes the intron sequences from the unspliced RNA sequence."""
	sequence_dict = extract_sequences(filename)
	dna_sequence = sequence_dict.pop('dna_sequence')
	for seq_id in sequence_dict:
		dna_sequence = dna_sequence.replace(sequence_dict[seq_id], '')
	return dna_sequence
	
def transcribe(dna_seq):
	"""Turns a DNA sequence into its RNA sequence"""
	rna_seq = ''
	for dna_nuc in dna_seq.upper():
		if dna_nuc == 'T':
			rna_nuc = 'U'
		else:
			rna_nuc = dna_nuc
		rna_seq += rna_nuc
	return rna_seq

def translate(rna_seq):
	"""returns the protein sequence for a given RNA sequence"""
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
	
def splice_transcribe_translate(filename):
	"""Extracts DNA sequences from a file (where the first sequence is
	the sequence containing introns and exons), removes the introns (all 
	other sequences in the file, transcribes the DNA into RNA, translates
	the RNA into protein and returns the protein sequence."""
	dna_sequence = remove_introns(filename)
	rna_sequence = transcribe(dna_sequence)
	protein_sequence = translate(rna_sequence)
	print(protein_sequence)
