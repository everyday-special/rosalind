"""
Cows for the cattle breeder game
"""

import pygame
import threading
from pygame.sprite import Sprite

import random

class Cow(Sprite):
	"""A class to represent a single cow"""
	
	def __init__(self, cb_settings, genotypes_1, genotypes_2, screen):
		"""Initializes the cow and its starting position"""
		super(Cow, self).__init__()
		self.screen = screen
		
		# Random color genotype
		self.color_genotype = (genotypes_1.color_genotype[random.randint(0, (len(genotypes_1.color_genotype) - 1))], genotypes_2.color_genotype[random.randint(0, (len(genotypes_2.color_genotype) - 1))])
		self.size_genotype = (genotypes_1.size_genotype[random.randint(0, (len(genotypes_1.size_genotype) - 1))], genotypes_2.size_genotype[random.randint(0, (len(genotypes_2.size_genotype) - 1))])
		
		# Cow movement related variables
		self.x_direction = random.randint(-1, 1)
		self.y_direction = random.randint(-1, 1)
		self.move_counter = random.randint(0, 10)
		self.drag = False
		self.dead = False
		
		# Get correct size phenotype and health based on genotype
		if 'small' in self.size_genotype:
			if 'large' in self.size_genotype:
				self.size_phenotype = 'medium_cow'
				self.health = 80
				self.max_health = 80
			else:
				self.size_phenotype = 'small_cow'
				self.health = 60
				self.max_health = 60
		elif 'large' in self.size_genotype:
			self.size_phenotype = 'big_cow'
			self.health = 100
			self.max_health = 100
		
		# Get the correct color phenotype based on genotype
		if 'blue' in self.color_genotype:
			if 'red' in self.color_genotype:
				self.color_phenotype = 'purple_cow'
			elif 'yellow' in self.color_genotype:
				self.color_phenotype = 'green_cow'
			else:
				self.color_phenotype = 'blue_cow'
		elif 'red' in self.color_genotype:
			if 'yellow' in self.color_genotype:
				self.color_phenotype = 'orange_cow'
			else:
				self.color_phenotype = 'red_cow'
		elif 'yellow' in self.color_genotype:
			self.color_phenotype = 'yellow_cow'
		elif 'white' in self.color_genotype:
			if 'black' in self.color_genotype:
				self.color_phenotype = 'black_spots_white_cow'
			elif 'brown' in self.color_genotype:
				self.color_phenotype = 'brown_spots_white_cow'
			else:
				self.color_phenotype = 'white_cow'
		elif 'brown' in self.color_genotype:
			if 'black' in self.color_genotype:
				self.color_phenotype = 'black_spots_brown_cow'
			else:
				self.color_phenotype = 'brown_cow'
		elif 'black' in self.color_genotype:
			self.color_phenotype = 'black_cow'
		
		# Load cow image and get its rect
		self.image = pygame.image.load('images/'+ self.size_phenotype + '/' + self.color_phenotype + '.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Create random position for cow
		self.rect.centerx = random.randint(20, (cb_settings.screen_width - 20))
		self.rect.centery = random.randint(20, (cb_settings.screen_height - 20))
	
		# Make health bar
		# Set color of health bar
		self.health_bar_color = (0, 0, 0)
		# Build the rect and position it above cow
		self.health_bar = pygame.Rect(0, 0, self.rect.width, 6)
		self.health_bar.centerx = self.rect.centerx
		self.health_bar.bottom = self.rect.top - 2
	
	def update_health_bar(self):
		"""updates the position and size of the cows health bar"""
		self.health_bar.centerx = self.rect.centerx
		self.health_bar.bottom = self.rect.top - 2
		
	
	def blitme(self, herd, wolf_pack):
		"""draw the cow at its current location"""
		self.screen.blit(self.image, self.rect)
		if self.dead == False:
			if self.health != self.max_health:
				self.update_health_bar()
				self.fill_health_bar(herd)
				self.screen.fill(self.health_bar_color, self.health_bar)
				self.screen.fill(self.health_bar_fill_color, self.health_bar_fill)
	
	def fill_health_bar(self, herd):
		"""Fills cows health bar, removes cow from herd if health reaches zero"""
		self.health_ratio = self.health / self.max_health
		# Set health color
		if self.health_ratio > .66:
			self.health_bar_fill_color = (0, 255, 0) # green = healthy
		elif self.health_ratio > .33:
			self.health_bar_fill_color = (255, 255, 0) # yellow = not so healthy
		elif self.health_ratio > 0:
			self.health_bar_fill_color = (255, 0, 0) # red = near death
		elif self.health_ratio <= 0:
			self.dead = True
		self.health_bar_fill = pygame.Rect(0, 0,(self.health_ratio * self.rect.width) - 2, 4)
		# Position health_bar_fill inside health_bar
		self.health_bar_fill.left = self.health_bar.left + 1
		self.health_bar_fill.centery = self.health_bar.centery
		
		
