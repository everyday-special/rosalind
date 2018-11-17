"""
Solution for Rabbits and Recurrence Relations
This is the fourth problem in Project Rosalind's Bioinformatics Stronghold
Coded in Python
"""

def wascally_wabbits(months, litter_size):
	"""Returns the total number of rabbit pairs that will be present after
	a given amount of months (months), beginning with 1 pair producing litters of
	a given amount of rabbit pairs (litter_size). Uses the following assumptions:
	-The population begins in the first month with a pair of newborn rabbits.
	-Rabbits reach reproductive age after one month.
	-In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
	-Exactly one month after two rabbits mate
	-Litters are of a given size and consist of an equal amount of males and females
	-Rabbits never die or stop reproducing.
	"""
	# Initial amount of rabbts
	mature_pairs = 0
	young_pairs = 1
	new_born_pairs = 0
	time = 1
	while time < months:
		# create new rabbits
		new_born_pairs = mature_pairs * litter_size
		# increase to rabbits to next stage and reset amount in prior stage
		mature_pairs += young_pairs 
		young_pairs = 0
		young_pairs += new_born_pairs
		new_born_pairs = 0
		# increase time
		time += 1
	# calculate and return total amount of pairs
	total_pairs = new_born_pairs + young_pairs + mature_pairs
	return total_pairs
