
def find_motif(dna_sequence, motif):
	"""Finds all locations of the motif in the DNA sequence. Returns the
	index location of the beginning of each motif in the DNA sequence.
	Note: Project Rosalind requests 1-based index numbering as opposed to
	0-based index numbering"""
	motif_locations = []
	motif_locations_string = ''
	for i in range(len(dna_sequence)):
		if dna_sequence[i : i + len(motif)] == motif:
			# append 'i + 1' not 'i' to account for 1-based index numbering
			motif_locations.append(str(i + 1))
	for location in motif_locations:
		# Put each location in a string separated by a space for answer formatting
		motif_locations_string += (location + ' ')
	print(motif_locations_string)
