import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from input_text import InputText
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
import game_functions

import preprocessing


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	stats = GameStats(ai_settings)
	
	introduction_of_game = []
	preprocessing.introduction_of_game_prep(ai_settings, screen, introduction_of_game)
	
	next_button = Button(ai_settings, screen, "Next")
	preprocessing.next_button_prep(next_button, stats, introduction_of_game)
	back_button = Button(ai_settings, screen, "Back")
	preprocessing.back_button_prep(back_button, next_button)
	
	username_input_text = InputText(ai_settings, screen, "Username")
	
	username_confirm = Button(ai_settings, screen, "Confirm")
	preprocessing.username_confirm_button_prep(username_confirm, username_input_text)
	
	play_button = Button(ai_settings, screen, "Play")
	preprocessing.play_button_prep(play_button)
	
	score_board = ScoreBoard(ai_settings, screen, stats)
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	game_functions.create_fleet(ai_settings, screen, ship, aliens)
	clock = pygame.time.Clock()
	
	while True:
		clock.tick(ai_settings.ship_speed_factor * 300)
		game_functions.check_events(ai_settings, screen, stats, introduction_of_game, next_button, back_button, username_input_text, username_confirm, score_board, play_button, ship, aliens, bullets)
		if stats.input_username:
			if stats.game_active:
				ship.update()
				game_functions.update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets)
				game_functions.update_aliens(ai_settings, stats, screen, score_board, ship, aliens, bullets)
		game_functions.update_screen(ai_settings, screen, stats, introduction_of_game, next_button, back_button, username_input_text, username_confirm, score_board, ship, aliens, bullets, play_button)


run_game()
