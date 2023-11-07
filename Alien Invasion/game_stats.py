import json


class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.input_username = False
		self.game_active = False
		self.username_start_input = False
		self.score = 0
		self.level = 1
		with open("high score data.json", 'r') as high_score_data_file:
			high_score_data = json.load(high_score_data_file)
		if 'high score' in high_score_data:
			self.high_score = high_score_data['high score']
		else:
			self.high_score = 0
		if 'user' in high_score_data:
			self.high_score_user = high_score_data['user']
		else:
			self.high_score_user = None
	
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1