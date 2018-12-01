
import pygame.font

class Scoreboard():
	"""A class to report scoring information"""
    
	def __init__(self, cb_settings, screen):
		"""initialize scoreboard attributes"""
		self.cb_settings = cb_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		# Font settings and information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# Prepare the initial score image
		self.prep_score()
        
	def prep_score(self):
		"""Turn the score into a rendered image"""
		score_str = '$' + str(self.cb_settings.score)
		self.score_image = self.font.render(score_str, True, self.text_color)
		# Display the score in the upper right corner of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def show_score(self):
		"""Draw the score onto the screen"""
		self.screen.blit(self.score_image, self.score_rect)
