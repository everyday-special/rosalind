"""My Solution for Calculating Protein Mass
Problem from Project Rosalind Bioinformatics Stronghold
Returns the mass of a given protein sequence using monoisotopic masses
of each amino acid."""

def calculate_protein_mass(protein):
	"""Calculates the mass of a given protein sequence using
	monoisotopic masses of each amino acid"""
	amino_acid_mass_dict = {
		'F' : 147.06841, # Phenylalanine
		'L' : 113.08406, # Leucine
		'S' : 87.03203, # Serine
		'Y' : 163.06333, # Tyrosine
		'C' : 103.00919, # Cysteine
		'W' : 186.07931, # Tryptophan
		'P' : 97.05276, # Proline
		'H' : 137.05891, # Histidine
		'Q' : 128.05858, # Glutamine
		'R' : 156.10111, # Arginine
		'I' : 113.08406, # Isoleucine
		'M' : 131.04049, # Methionine
		'T' : 101.04768, # Threonine
		'N' : 114.04293, # Asparagine
		'K' : 128.09496, # Lysine
		'V' : 99.06841, # Valine
		'A' : 71.03711, # Alanine
		'D' : 115.02694, # Aspartic Acid
		'E' : 129.04259, # Glutamic Acid
		'G' : 57.02146 # Glycine
		}
	
	protein_mass = 0
	for amino_acid in protein.upper():
		protein_mass += amino_acid_mass_dict[amino_acid]
	
	return protein_mass
