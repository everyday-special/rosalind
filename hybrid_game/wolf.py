"""
Wolves for the cattle breeder game
"""

import pygame
import math
import threading

from pygame.sprite import Sprite

import random

class Wolf(Sprite):
	"""a class to represent a wolf"""
	
	def __init__(self, cb_settings, screen):
		"""initializes a wolf at its starting position"""
		super(Wolf, self).__init__()
		self.screen = screen
		self.cb_settings = cb_settings
		self.wolf_hit = False
		self.attack_ready = True
		
		# Load image and get its rectangle
		self.image = pygame.image.load('images/wolf/right_wolf.png')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		# Put wolf at a random position on the size
		self.side = random.randint(0, 3) # 0 = top, 1 = right side, 2 = bottom, 3 = left side
		if self.side == 0:
			# put wolf at a random spot on the top of the screen
			self.rect.centerx = random.randint(0, self.cb_settings.screen_width - 1)
			self.rect.top = self.screen_rect.top + 1
		elif self.side == 1:
			# put wolf at a random spot on the right side of the screen
			self.rect.right = self.screen_rect.right -1
			self.rect.centery = random.randint(0, self.cb_settings.screen_height - 1)
			self.image = pygame.image.load('images/wolf/left_wolf.png')
		elif self.side == 2:
			# put wolf at a random spot on the bottom of the screen
			self.rect.centerx = random.randint(0, self.cb_settings.screen_width - 1)
			self.rect.bottom = self.screen_rect.bottom - 1
		elif self.side == 3:
			# put wolf at a random spot on the left side of the screen
			self.rect.left = self.screen_rect.left
			self.rect.centery = random.randint(0, self.cb_settings.screen_height - 1)
			
	def blitme(self):
		"""Draw a wolf on the screen"""
		self.screen.blit(self.image, self.rect)
		
	def track_cow(self, herd):
		"""identifies and returns the cow closest to the wolf"""
		# max distance = hypotenuse of screen
		closest_distance = math.sqrt(self.cb_settings.screen_width ** 2 + self.cb_settings.screen_height ** 2)
		for cow in herd:
			# Checks all cows in herd to see which is closest
			x_dist = self.rect.centerx - cow.rect.centerx
			y_dist = self.rect.centery - cow.rect.centery
			cow_distance = math.sqrt(x_dist ** 2 + y_dist ** 2)
			if cow_distance < closest_distance and cow.dead == False:
				closest_distance = cow_distance
				closest_cow = cow
		return closest_cow
		
	def move_horizontally_towards_cow(self, closest_cow):
		"""moves left or right towards the closest cow"""
		if self.rect.centerx > closest_cow.rect.centerx:
			# move left and load image of left facing wolf
			self.image = pygame.image.load('images/wolf/left_wolf.png')
			self.rect.centerx -= 1
		elif self.rect.centerx < closest_cow.rect.centerx:
			# move right and load image of right facing wolf
			self.image = pygame.image.load('images/wolf/right_wolf.png')
			self.rect.centerx += 1
	
	def move_vertically_towards_cow(self, closest_cow):
		"""moves up or down towards the closest cow"""
		if self.rect.centery > closest_cow.rect.centery:
			# move up
			self.rect.centery -= 1
		elif self.rect.centery < closest_cow.rect.centery:
			# move down
			self.rect.centery += 1
			
	def attack_cow(self, cow):
		"""attacks the closest cow"""
		if self.attack_ready == True:
			if self.rect.centerx > cow.rect.centerx:
				# load image of left facing attacking wolf
				self.image = pygame.image.load('images/wolf/left_wolf_attack.png')
				image_reset_timer = threading.Timer(1.0, self.reset_left_image)
				image_reset_timer.start()
			elif self.rect.centerx <= cow.rect.centerx:
				# load image of right facing attacking wolf
				self.image = pygame.image.load('images/wolf/right_wolf_attack.png')
				image_reset_timer = threading.Timer(1.0, self.reset_right_image)
				image_reset_timer.start()
			cow.health -= 20
			self.attack_ready = False
			attack_timer = threading.Timer(3.0, self.reset_attack)
			attack_timer.start()

	def reset_attack(self):
		"""allows the wolf to attack again"""
		self.attack_ready = True
	
	def reset_left_image(self):
		"""resets the wolf's image to not be attacking"""
		# load image of left facing wolf
		self.image = pygame.image.load('images/wolf/left_wolf.png')
	
	def reset_right_image(self):
		"""resets the wolf's image to not be attacking"""
		# load image of right facing wolf
		self.image = pygame.image.load('images/wolf/right_wolf.png')
