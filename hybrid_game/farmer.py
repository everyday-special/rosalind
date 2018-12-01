

import pygame

class Farmer():

	def __init__(self, screen):
		"""initializes farmer in center of pasture"""
		self.screen = screen
		
		# Load the farmer image and get its rectangle
		self.image = pygame.image.load('images/farmer/farmer.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
        
        # Farmer movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
		# Start the Farmer in the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		
	def blitme(self):
		"""Draws farmer at current position"""
		self.screen.blit(self.image, self.rect)
		
	def update_location(self):
		"""Updates the farmers position"""
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x < self.screen_rect.right and mouse_x > self.screen_rect.left:
			self.rect.centerx = mouse_x
		if mouse_y < self.screen_rect.bottom and mouse_y > self.screen_rect.top:
			self.rect.centery = mouse_y
	
				
		
