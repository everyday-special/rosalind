"""My Solution for Partial Permutations
Problem from Project Rosalind Bioinformatics Stronghold
Returns the number of partial permutations of k objects from a
collection of n objects. In other words, calculates and returns nPk."""

def fact(number, m):
	"""Returns the factorial of a number"""
	if number == m:
		# stop at m
		return 1
	else:
		# multiplies all numbers below the given number until m
		return number * fact(number - 1, m)

def partial_permute(n, k):
	"""Returns the total amount of partial permutations of k objects out
	of a collection of n objects."""
	m = n - k
	return fact(n, m) % 10 ** 6
