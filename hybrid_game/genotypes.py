"""
Contains the genotypes for Cattle Breeder game.
"""

import pygame

class Genotypes():
	"""A class to store the available genotypes for the cows"""
	
	def __init__(self):
		"""Initializes genotype settings"""
		self.color_genotype = ['white', 'black', 'brown', 'blue', 'yellow', 'red',]
		self.size_genotype = ['small', 'large']
