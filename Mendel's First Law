"""
My Solution for Mendels First Law
This is the 7th problem in Project Rosalind's Bioinformatics Stronghold
"""

def probability_of_dominant_offspring(k, m, n):
	"""
	Given 3 integers representing the amount of homozygous dominant (k),
	heterozygous (m), and homozygous recessive (n) individuals in a 
	population for a given trait, returns the probability that two randomly
	selected indivudals produce an offspring with a dominant allele/dominant
	phenotype. D is the dominant allele and d is the recessive allele
	"""
	total_pop = k + m + n
	
	# This equation came from adding up the probability of each individual
	# mating and reproduction that could result in a dominant offspring (DD or Dd)
	total_probability = ((k ** 2 - k) + (2 * k * m) + (3 / 4 * (m ** 2 - m)) + (2* k * n) + (m * n)) / (total_pop ** 2 - total_pop)
	
	return total_probability
