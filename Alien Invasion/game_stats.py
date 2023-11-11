import json


class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.input_username = False
		self.game_active = False
		self.username_start_input = False
		self.high_score = 0
		self.score = 0
		self.level = 1
		self.view_introduction = True
		self.introduction_page = 0
		
		self.back_button = False
		
		self.user = None
		
		with open("high score data.json", 'r') as high_score_data_file:
			high_score_data = json.load(high_score_data_file)
			if 'high score' in high_score_data:
				self.high_score_history = high_score_data['high score']
			else:
				self.high_score_history = 0
			if 'user' in high_score_data:
				self.high_score_history_user = high_score_data['user']
			else:
				self.high_score_history_user = None
	
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1