import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from input_text import InputText
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
import game_functions


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion-1")
	
	stats = GameStats(ai_settings)
	username_input_text = InputText(ai_settings, screen, "Username")
	
	username_confirm = Button(ai_settings, screen, "Confirm")
	username_confirm.rect.centerx = username_confirm.screen_rect.centerx
	username_confirm.rect.top = username_input_text.rect.bottom + 10
	username_confirm.msg_image_rect.center = username_confirm.rect.center
	
	play_button = Button(ai_settings, screen, "Play")
	play_button.rect.center = play_button.screen_rect.center
	play_button.msg_image_rect.center = play_button.rect.center
	
	score_board = ScoreBoard(ai_settings, screen, stats)
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	game_functions.create_fleet(ai_settings, screen, ship, aliens)
	clock = pygame.time.Clock()
	
	while True:
		clock.tick(ai_settings.ship_speed_factor * 300)
		game_functions.check_events(ai_settings, screen, stats, username_input_text, username_confirm, score_board, play_button, ship, aliens, bullets)
		if stats.input_username:
			if stats.game_active:
				ship.update()
				game_functions.update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets)
				game_functions.update_aliens(ai_settings, stats, screen, score_board, ship, aliens, bullets)
		game_functions.update_screen(ai_settings, screen, stats, username_input_text, username_confirm, score_board, ship, aliens, bullets, play_button)


run_game()
