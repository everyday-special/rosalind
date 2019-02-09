"""
Solution for Rabbits and Recurrence Relations
This is the fourth problem in Project Rosalind's Bioinformatics Stronghold
Coded in Python

Solved using recurence
"""

def rabbits(n,k):
	"""Returns the total number of rabbit pairs that will be present after
	a given amount of months (n), beginning with 1 pair producing litters of
	a given amount of rabbit pairs (k). Uses the following assumptions:
	-The population begins in the first month with a pair of newborn rabbits.
	-Rabbits reach reproductive age after one month.
	-In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
	-Exactly one month after two rabbits mate
	-Litters are of a given size and consist of an equal amount of males and females
	-Rabbits never die or stop reproducing.
	"""
	if n <= 2:
		return 1
	else:
		return rabbits(n - 1, k) + rabbits(n - 2, k) * k
