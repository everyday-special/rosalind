"""
Solution for Open Reading Frames
From Project Rosalind's Bioinformatics Stronghold
Takes a file containing a single FASTA formatted DNA sequence of at most
1 kbp and returns all the unique open reading frames from that sequece 
and its reverse complement.
Assumes the FASTA formatting is in the form of '>Rosalind_####' 
All you need to do is run the function 'open_reading_frames' with the
file name it will return all the unique open reading frames
"""

def extract_sequence_from_file(filename):
	"""opens file and extracts the DNA sequence"""
	with open(filename) as f:
		sequence = f.read().split()
	sequence = ''.join(sequence)
	sequence = sequence[14:]
	return sequence

def dna_to_rna(dna):
	"""returns the RNA sequence for a given DNA sequence"""
	rna_sequence = ''
	for nucleotide in dna.upper(): # switches in U for T
		if nucleotide == 'T':
			rna_sequence += 'U'
		else:
			rna_sequence += nucleotide
	return rna_sequence
			
def open_reading_frames(filename):
	"""returns all the open reading frames in a given file containing a
	 DNA sequence and its reverse complement sequence"""
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
	dna_sequence = extract_sequence_from_file(filename)
	rna_sequence = dna_to_rna(dna_sequence) # generates RNA of DNA sequence
	rev_comp_dna = complement_dna(dna_sequence) # generates reverse complement of DNA sequence
	rev_comp_rna = dna_to_rna(rev_comp_dna) # generates rna of reverse complement DNA
	orf_list = [] # final list of open reading frames
	orf_list += find_open_reading_frames(rna_sequence, rna_codon_dict) # finds all open reading frames in RNA sequece
	orf_list += find_open_reading_frames(rev_comp_rna, rna_codon_dict) # finds all open reading frames in reverse complement RNA sequence
	display_protein_list(orf_list) # prints each distinct open reading frames in the right format
	
def display_protein_list(protein_list):
	"""displays only the distinct proteins in the protein list in the correct format"""
	protein_set = set(protein_list) # removes duplicates
	for protein in protein_set:
		print(protein) # prints each ORF

def find_open_reading_frames(rna_sequence, rna_codon_dict):
	"""Finds all open reading frames in a DNA sequence"""
	protein_list = [] # list of open reading frames in this sequence
	protein_sequence = ''
	counter = 0 # couter for iterating through ORF
	open_reading_frame = False # switch for when an open reading frame is found/ends
	for i in range(0, len(rna_sequence)):
		if rna_sequence[i : i + 3] == 'AUG': # turns open reading frame switch on when start codon is found
			open_reading_frame = True
			counter = i
		while open_reading_frame == True:
			codon = rna_sequence[counter : counter + 3] # finds the codon
			if codon in rna_codon_dict['Stop']: # if stop codon is encountered
				open_reading_frame = False
				protein_list.append(protein_sequence)
				protein_sequence = ''
				counter = 0
			elif counter >= len(rna_sequence): # if ORF goes past the end of the sequence
				protein_sequence = ''
				counter = 0
				open_reading_frame = False
			else:
				for amino_acid in rna_codon_dict: # adds the correct amino acid using the codon table
					if codon in rna_codon_dict[amino_acid]:
						protein_sequence += amino_acid
			counter += 3 # moves the couter forward one codon (3 nucleotides)
	return protein_list # returns list of ORFs
	
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
