"""
Settings for the cattle breeder game.
"""

class Settings():
	"""A class to store the settings for Cattle Breeder"""
	
	def __init__(self):
		"""Initialize game settings"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (80, 230, 80)
		self.text_color = (30, 30, 30)
		
		# General game settings
		self.initial_herd_size = 2
		self.cow_speed_factor = 1
		self.score = 0
		self.active = False
		self.game_over = False
		self.win = False
