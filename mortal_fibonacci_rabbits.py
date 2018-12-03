"""
Solution for Moral Fibonacci Rabbits
This is the 11th problem in Project Rosalind's Bioinformatics Stronghold
"""

def wascally_wabbits(n, m):
	"""Returns the total number of rabbit pairs that will be present after
	a given amount of months (n), beginning with 1 pair producing litters of
	2 rabbits. Rabbits die after m months. Uses the following assumptions:
	-The population begins in the first month with a pair of newborn rabbits.
	-Rabbits reach reproductive age after one month.
	-In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
	-Litters consist of one male and one female
	-Rabbits die after m months.
	"""
	# Initial amount of rabbit pairs
	rabbits = [0 for month in range(m + 1)] # rabbits[0] = new born rabbits, rabbits[1] = immature rabbits, rabbits[2:] are mature rabbits, rabbits[-1] = rabbits right before dying
	rabbits[1] = 1
	time = 1
	while time < n:
		# create new rabbits
		mature_pairs = 0
		for rabbit_pairs in rabbits[2:]:
			mature_pairs += rabbit_pairs
		rabbits[0] = mature_pairs
		# increase to rabbits to next stage and reset amount in prior stage
		rabbits[m] = 0
		i = m -1
		while i >= 0:
			rabbits[i + 1] = rabbits[i]
			i -= 1
		rabbits[0] = 0
		# increase time
		time += 1
	# calculate and return total amount of pairs
	total_pairs = 0
	for rabbit_pairs in rabbits:
		total_pairs += rabbit_pairs
	return total_pairs

