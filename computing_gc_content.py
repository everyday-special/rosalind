"""
Solution for Computing GC Content
This is the fifth problem in Project Rosalind's Bioinformatics Stronghold
"""

def compute_gc_content():
	"""
	Prints the sequence ID and the gc content of several dna sequences
	in a fasta formatted file
	"""
	with open('rosalind_gc.txt') as f:
  
  
		# convert file contents into dictionary of 4 number sequence id and sequence
		# there is likely a more efficient way to do this
		sequence_list = f.read().split()
		sequence_list = ''.join(sequence_list)
		sequence_list = sequence_list.split('>Rosalind_')
		del sequence_list[0] # first item in sequence_list is an empty string
		sequence_dict = {}
		for sequence in sequence_list:
			sequence_dict[sequence[:4]] = sequence[4:] # creates the dictionary where the key is the 4 digit sequence ID and the value is the sequence
      
      
		for seq_id in sequence_dict:
			gc_count = 0
			for base in sequence_dict[seq_id].upper():
				# counts amount of C and G
				if base == 'C':
					gc_count += 1
				elif base == 'G':
					gc_count += 1
			gc_content = gc_count / len(sequence_dict[seq_id]) * 100 # calculate GC content as a percentage
			print('Rosalind_' + seq_id)
			print(gc_content)
