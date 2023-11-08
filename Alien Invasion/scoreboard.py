import pygame.font
from pygame.sprite import Group

from ship import Ship


class ScoreBoard():
	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		
		self.prep_high_score_history()
		self.prep_high_score_history_user()
		self.prep_high_score()
		self.prep_score()
		self.prep_level()
		self.prep_user()
		self.prep_ships()
	
	def prep_score(self):
		round_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(round_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = self.high_score_rect.bottom + 10
	
	def show_score(self):
		self.screen.blit(self.high_score_history_image, self.high_score_history_rect)
		self.screen.blit(self.high_score_history_user_image, self.high_score_history_user_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.user_image, self.user_rect)
		
		self.ships.draw(self.screen)
	
	def prep_high_score_history(self):
		high_score_history = int(round(self.stats.high_score_history, -1))
		high_score_history_str = "{:,}".format(high_score_history)
		self.high_score_history_image = self.font.render(high_score_history_str, True, self.text_color, self.ai_settings.bg_color)
		
		self.high_score_history_rect = self.high_score_history_image.get_rect()
		self.high_score_history_rect.centerx = self.screen_rect.centerx
		self.high_score_history_rect.top = self.screen_rect.top
	
	def prep_high_score_history_user(self):
		self.high_score_history_user_image = self.font.render(self.stats.high_score_history_user, True, self.text_color, self.ai_settings.bg_color)
		
		self.high_score_history_user_rect = self.high_score_history_user_image.get_rect()
		self.high_score_history_user_rect.centerx = self.screen_rect.centerx
		self.high_score_history_user_rect.top = self.high_score_history_rect.bottom + 10
	
	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom + 10
	
	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	
	def prep_user(self):
		self.user_image = self.font.render(self.stats.user, True, self.text_color, self.ai_settings.bg_color)
		
		self.user_rect = self.user_image.get_rect()
		self.user_rect.right = self.screen_rect.right - 20
		self.user_rect.top = self.level_rect.bottom + 10
	
	def prep_high_score(self):
		self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, self.ai_settings.bg_color)
		
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 20
		self.high_score_rect.top = 20
