"""
Contains the game functions for Cattle Breeder
"""
import random
import pygame
import sys

from button import Button
from cows import Cow
from wolf import Wolf

def create_initial_herd(cb_settings, genotypes, herd, screen):
	"""Creates your initial herd"""
	# Creates the initial herd and places them randomly in the pasture
	for cow in range(cb_settings.initial_herd_size):
		# Create each cow
		cow = Cow(cb_settings, genotypes, genotypes, screen)
		herd.add(cow)

def update_screen(cb_settings, farmer, herd, lose_button, play_button, sb, screen, win_button, wolf_pack):
	"""updates the screen"""
	screen.fill(cb_settings.bg_color)
	farmer.update_location()
	if cb_settings.active == True:
		wolf_appear(cb_settings, screen, wolf_pack)
	for wolf in wolf_pack:
		wolf.blitme()
	for cow in herd:
		cow.blitme(herd, wolf_pack)
	# Draw buttons if game is inactive
	if cb_settings.active == False:
		play_button.draw_button()
		if cb_settings.game_over == True and cb_settings.win == True:
			win_button.draw_button()
		elif cb_settings.game_over == True and cb_settings.win == False:
			lose_button.draw_button()
	farmer.blitme()
	sb.prep_score()
	sb.show_score()

def cow_behavior(cb_settings, herd):
	"""Determines cow's behavior: moving or staying still"""
	for cow in herd:
		if cow.dead == True:
			cow_dead(cow, herd)
		elif cow.move_counter < 5:
			# Move around
			move_cow_around(cb_settings, cow)
		elif cow.move_counter == 500:
			# Change direction
			change_cow_direction(cow)
			cow.move_counter = 0
		elif cow.drag == True:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			cow.rect.centerx = mouse_x
			cow.rect.centery = mouse_y
		if cow.drag == False:
			cow.move_counter += 1
			
def cow_dead(cow, herd):
	"""Turns dead cow into ghost and moves them off the screen"""
	cow.image = pygame.image.load('images/' + cow.size_phenotype + '/ghost_cow.png')
	if cow.rect.top <= cow.screen_rect.top:
		# remove cow
		herd.remove(cow)
	else:
		cow.rect.top -= 1

def move_cow_around(cb_settings, cow):
	"""Move the cow based on its speed factor and direction"""
	if cow.x_direction == -1 and cow.rect.left > cow.screen_rect.left:
		cow.rect.centerx += (cb_settings.cow_speed_factor * cow.x_direction)
	elif cow.x_direction == 1 and cow.rect.right < cow.screen_rect.right:
		cow.rect.centerx += (cb_settings.cow_speed_factor * cow.x_direction)
	elif cow.y_direction == -1 and cow.rect.top > cow.screen_rect.top:
		cow.rect.centery += (cb_settings.cow_speed_factor * cow.y_direction)
	elif cow.y_direction == 1 and cow.rect.bottom < cow.screen_rect.bottom:
		cow.rect.centery += (cb_settings.cow_speed_factor * cow.y_direction)
	
def change_cow_direction(cow):
	"""random change the cows direction"""
	cow.x_direction = random.randint(-1, 1)
	cow.y_direction = random.randint(-1, 1)

def check_events(cb_settings, farmer, herd, genotypes, play_button, screen, wolf_pack):
	"""Responds to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(cb_settings, event, farmer, herd, genotypes, screen, wolf_pack)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if cb_settings.active == True:
				check_cow_click(event, herd, mouse_x, mouse_y)
			if cb_settings.active == False:
				check_play_button(cb_settings, genotypes, herd, play_button, screen, wolf_pack, mouse_x, mouse_y)
		elif event.type == pygame.MOUSEBUTTONUP and cb_settings.active == True:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_cow_click(event, herd, mouse_x, mouse_y)
			
def check_play_button(cb_settings, genotypes, herd, play_button, screen, wolf_pack, mouse_x, mouse_y):
	"""Checks to see if the play button was clicked"""
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		if cb_settings.game_over == True:
			herd.empty()
			wolf_pack.empty()
			cb_settings.score = 0
			cb_settings.game_over = False
			create_initial_herd(cb_settings, genotypes, herd, screen)
		cb_settings.active = True
			
def check_cow_click(event, herd, mouse_x, mouse_y):
	for cow in herd:
		cow_clicked = cow.rect.collidepoint(mouse_x, mouse_y)
		if cow_clicked and event.type == pygame.MOUSEBUTTONDOWN:
			cow.drag = True
			break
		if cow_clicked and event.type == pygame.MOUSEBUTTONUP:
			cow.drag = False

def check_keydown_events(cb_settings, event, farmer, herd, genotypes, screen, wolf_pack):
	"""checks for keydown events from player"""
	if event.key == pygame.K_q:
		# Press q to quit
		pygame.quit()
		sys.exit()
	elif event.key == pygame.K_SPACE and cb_settings.active == True:
		make_baby(cb_settings, herd, screen)
		farmer_attack(farmer, wolf_pack)
	elif event.key == pygame.K_s:
		sell_cow(cb_settings, herd)
	elif event.key == pygame.K_b:
		buy_cow(cb_settings, herd, genotypes, screen)
	elif event.key == pygame.K_w:
		wolf = Wolf(cb_settings, screen)
		wolf_pack.add(wolf)
	elif event.key == pygame.K_p:
		if cb_settings.active == False:
			cb_settings.active = True
		elif cb_settings.active == True:
			for cow in herd:
				if cow.drag == True:
					cow.drag = False # Farmer drops cow he is currently dragging when game is paused
			cb_settings.active = False
		
		
def make_baby(cb_settings, herd, screen):
	"""Breeds two selected cows"""
	mouse_x, mouse_y = pygame.mouse.get_pos()
	cow_1_exists = False
	# Get mating pair
	for cow in herd:
		if cow.drag == True:
			cow_1 = cow
			cow_1_exists = True
			break
	for cow in herd:
		if cow.drag == False and cow.rect.collidepoint(mouse_x, mouse_y) and cow_1_exists == True: # Prevents trying to create a new cow if now cow is selected for cow_1
			cow_2 = cow
			# Create new cow and add to the herd
			new_cow = Cow(cb_settings, cow_1, cow_2, screen)
			herd.add(new_cow)
			break
	
def sell_cow(cb_settings, herd):
	"""sells selected cow for money"""
	for cow in herd:
		if cow.drag == True:
			if (len(herd.sprites()) > 2) or (len(herd.sprites()) > 1 and cb_settings.score >= 200):
				# 100 points for thorougbred cow
				if cow.color_genotype[0] == cow.color_genotype[1]:
					cb_settings.score += 100
				# 50 points for non-thoroughbred cow
				elif cow.color_genotype[0] != cow.color_genotype[1]:
					cb_settings.score += 50
				herd.remove(cow)
				break

def buy_cow(cb_settings, herd, genotypes, screen):
	"""buys a new cow using money"""
	if cb_settings.score >= 200:
		cb_settings.score -= 200
		cow = Cow(cb_settings, genotypes, genotypes, screen)
		herd.add(cow)

def wolf_behavior(farmer, herd, wolf_pack):
	"""moves a wolves towards the cow closest to them"""
	for wolf in wolf_pack:
		if wolf.wolf_hit == False and len(herd.sprites()) > 0:
			closest_cow = wolf.track_cow(herd)
			if not pygame.sprite.collide_rect(closest_cow, wolf):
				wolf.move_horizontally_towards_cow(closest_cow)
				wolf.move_vertically_towards_cow(closest_cow)
			elif pygame.sprite.collide_rect(closest_cow, wolf):
				wolf.attack_cow(closest_cow)
		if wolf.wolf_hit == True:
			wolf_retreat(farmer, wolf, wolf_pack)

def farmer_attack(farmer, wolf_pack):
	"""farmer attacks the wolf he is near"""
	for wolf in wolf_pack:
		if pygame.sprite.collide_rect(farmer, wolf):
			if wolf.rect.centerx < farmer.rect.centerx:
				farmer.image = pygame.image.load('images/farmer/farmer_attack_left.png')
			elif wolf.rect.centerx > farmer.rect.centerx:
				farmer.image = pygame.image.load('images/farmer/farmer_attack_right.png')
			wolf.wolf_hit = True

def wolf_retreat(farmer, wolf, wolf_pack):
	"""wolf retreats to edge of screen, farmer returns to normal stance"""
	if wolf.rect.centerx < wolf.cb_settings.screen_width / 2:
		# retreat left
		wolf.image = pygame.image.load('images/wolf/left_wolf.png')
		wolf.rect.centerx -= 1
	elif wolf.rect.centerx > wolf.cb_settings.screen_width / 2:
		# retreat right
		wolf.image = pygame.image.load('images/wolf/right_wolf.png')
		wolf.rect.centerx += 1
	if wolf.rect.centery < wolf.cb_settings.screen_height / 2:
		# retreat up
		wolf.rect.centery -= 1
	elif wolf.rect.centery < wolf.cb_settings.screen_height / 2:
		# retreat down
		wolf.rect.centery += 1
	if wolf.rect.bottom >= wolf.screen_rect.bottom or wolf.rect.top <= wolf.screen_rect.top or wolf.rect.right >= wolf.screen_rect.right or wolf.rect.left <= wolf.screen_rect.left:
		# remove wolf if touching side of screen
		wolf_pack.remove(wolf)
		farmer.image = pygame.image.load('images/farmer/farmer.png')
		
def count_cows(cb_settings, herd, screen):
	"""Counts the remaining cows and calculates if the player has won or lost"""
	# Figures out if the player has lost
	if len(herd.sprites()) == 0 or (len(herd.sprites()) == 1 and cb_settings.score < 200):
		cb_settings.win = False
		cb_settings.active = False
		cb_settings.game_over = True
	# Figures out if the player has won
	list_of_cow_colors = []
	for cow in herd:
		list_of_cow_colors.append(cow.color_phenotype)
	if len(set(list_of_cow_colors)) == 12:
		cb_settings.win = True
		cb_settings.active = False
		cb_settings.game_over = True

def wolf_appear(cb_settings, screen, wolf_pack):
	"""Chance of radomly generating a wolf"""
	if random.randint(0, 10000) == 27: # 1 in 500 chance of wolf appearing
		wolf = Wolf(cb_settings, screen)
		wolf_pack.add(wolf)
