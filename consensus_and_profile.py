
def find_consensus_and_profile(filename):
	"""Prints a consensus string and profile matrix for a collection of
	DNA sequences from a file in FASTA format. In the case of multiple
	consensus sequences only one is returned."""
	
	with open(filename) as f:
		# convert file contents into dictionary of 4 digit sequence id and sequence
		sequence_list = f.read().split()
	sequence_list = ''.join(sequence_list)
	sequence_list = sequence_list.split('>Rosalind_')
	del sequence_list[0] # first item in sequence_list is an empty string
	sequence_dict = {}
	for sequence in sequence_list:
		# creates the dictionary where the key is the 4 digit identifier
		sequence_dict[sequence[:4]] = sequence[4:]
		seq_id = sequence[:4]
	sequence_length = len(sequence_dict[seq_id]) # get length of the sequences
	profile_matrix = find_profile_matrix(sequence_dict, sequence_length)
	consensus_sequence = find_consensus_sequence(profile_matrix)
	print(consensus_sequence)
	for nucleotide in profile_matrix:
		# Put each frequency in a string separated by a space for answer formatting
		frequency_string = ''
		for count in profile_matrix[nucleotide]:
			 frequency_string += ' ' + str(count)
		print(nucleotide + ':' + frequency_string)
	
def find_profile_matrix(sequence_dict, sequence_length):
	"""Returns a dictionary with 4 key : value pairs. The key is the
	nucleotide (A, T, C, or G) and the value is a string with the number
	of times the nucleotide appears in that position separated by spaces."""
	# Create dictionary with list of zeros for each nucleotide in the sequence
	profile_matrix = {
		'A' : [0 for item in range(sequence_length)],
		'C' : [0 for item in range(sequence_length)],
		'G' : [0 for item in range(sequence_length)],
		'T' : [0 for item in range(sequence_length)]
		}
	# Go through each sequence and add up the amount of times each nucleotide occurs at each index
	for sequence in sequence_dict:
		for index in range(len(sequence_dict[sequence])):
			if sequence_dict[sequence][index].upper() == 'A':
				profile_matrix['A'][index] += 1
			elif sequence_dict[sequence][index].upper() == 'C':
				profile_matrix['C'][index] += 1
			elif sequence_dict[sequence][index].upper() == 'G':
				profile_matrix['G'][index] += 1
			elif sequence_dict[sequence][index].upper() == 'T':
				profile_matrix['T'][index] += 1
	return profile_matrix

def find_consensus_sequence(profile_matrix):
	"""Returns a string with the/one of the consensus sequences for a given
	profile matrix."""
	consensus_sequence = ''
	for index in range(len(profile_matrix['A'])):
		max_value = 0
		max_nucleotide = ''
		for nucleotide in profile_matrix:
			if profile_matrix[nucleotide][index] > max_value:
				max_value = profile_matrix[nucleotide][index]
				max_nucleotide = nucleotide
		consensus_sequence += max_nucleotide
	return consensus_sequence
