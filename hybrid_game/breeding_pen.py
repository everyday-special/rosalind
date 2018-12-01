import pygame

class Breeding_Pen():
	"""Code for the breeding pen. Drag two cows to the breeding pen to have them
	produce a calf."""
	
	def __init__(self, cb_settings, screen): 
		"""initialize button attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		# Set the dimensions and properties of the breeding pen.
		self.width, self.height = 200, 100
		self.button_color = (139, 69, 19)
		# Build breeding pen and put it in upper left corner.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (self.width / 2, self.height / 2)
		# Build the slots
		self.slot_1 = []
		self.slot_1_rect = pygame.Rect(0, 0, self.width / 2  * 0.9, self.height * 0.9)
		self.slot_1_filled = False
		self.slot_2 = []
		self.slot_2_rect = pygame.Rect(0, 0, self.width / 2 * 0.9, self.height * 0.9)
		self.slot_2_filled = False
		# Put slots into pen
		self.slot_1_rect.center = (self.width / 4, self.height / 2)
		self.slot_2_rect.center = (3 * self.width / 4, self.height /2)
		

	def draw_breeding_pen(self, cb_settings):
		# Draw a empty breeding pen
		self.screen.fill(self.button_color, self.rect)
		self.screen.fill(cb_settings.bg_color, self.slot_1_rect)
		self.screen.fill(cb_settings.bg_color, self.slot_2_rect)
