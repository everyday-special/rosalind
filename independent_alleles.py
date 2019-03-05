"""
My Soluton for Independent Alleles from Project Rosalind's
Bioinformatics Stronghold.
"""

def fact(number):
	"""Returns the factorial of a number"""
	if number == 1 or number == 0:
		# 1! = 0! = 1
		return 1
	else:
		# multiplies all numbers below the given number
		return number * fact(number - 1)

def binomial_formula(k, n):
	"""
	Given: Two positive integers k (k≤7) and n (n≤2k). In this problem, 
	we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom
	has two children in the 1st generation, each of whom has two children, 
	and so on. Each organism always mates with an organism having genotype 
	Aa Bb.
	Return: The probability that at least N Aa Bb organisms will belong 
	to the k-th generation of Tom's family tree (don't count the Aa Bb 
	mates at each level). Assume that Mendel's second law holds for the 
	factors.
	Uses binomaial formula:
	b(x; n, P) = { n! / [x! (n - x)!]} * P ** x * (1 - P) ** (n - x)
	Where x = # of success, n = # of trials, and P = P(success)
	"""
	if n >= 2 ** k:
		# When the number of successes is equal to the total number of trials, end recursion
		return fact(2 ** k) / (fact(n) * fact((2 ** k) - n)) * (.25 ** n) * (.75 ** ((2 ** k) - n))
	
	else:
		# return the P(n AaBb offspring in that generation) + P(n + 1 AaBb offspring in that generation)
		return fact(2 ** k) / (fact(n) * fact((2 ** k) - n)) * (.25 ** n) * (.75 ** ((2 ** k) - n)) + binomial_formula(k, n + 1)
