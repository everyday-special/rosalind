"""
Code for the Hybrid Game for the Game Off 2018
A simple game. You play a rancher, managing a herd of cattle and breeding cattle.
Different traits display different patterns of heritability.
"""

import sys

import pygame
from pygame.sprite import Group

from farmer import Farmer
from settings import Settings
from cows import Cow
from genotypes import Genotypes
import game_functions as gf
from scoreboard import Scoreboard
from button import Button

def rungame():
	# Initialize game and create a screen object.
	pygame.init()
	cb_settings = Settings()
	genotypes = Genotypes()
	screen = pygame.display.set_mode((cb_settings.screen_width, cb_settings.screen_height))
	screen.fill(cb_settings.bg_color)
	pygame.display.set_caption('Cattle Breeder')
	farmer = Farmer(screen)
	
	# Make buttons
	play_button = Button(cb_settings, screen, 'PLAY', cb_settings.screen_height / 2)
	win_button = Button(cb_settings, screen, 'YOU WIN!!', cb_settings.screen_height / 4)
	lose_button = Button(cb_settings, screen, 'YOU LOSE', cb_settings.screen_height / 4)
	
	herd = Group()
	wolf_pack = Group()
	# Create intial herd
	gf.create_initial_herd(cb_settings, genotypes, herd, screen)
	sb = Scoreboard(cb_settings, screen)
	
	# Start the main game loop.
	while True:
		# Hide mouse cursor
		pygame.mouse.set_visible(False)
		gf.update_screen(cb_settings, farmer, herd, lose_button, play_button, sb, screen, win_button, wolf_pack)
		gf.check_events(cb_settings, farmer, herd, genotypes, play_button, screen, wolf_pack)
		if cb_settings.active:
		
			# Redraw screen during each pass through loop.
			gf.wolf_behavior(farmer, herd, wolf_pack)
			gf.cow_behavior(cb_settings, herd)
			gf.count_cows(cb_settings, herd, screen)
		
			# Make the most recently drawn screen visible.
		pygame.display.flip()

rungame()
