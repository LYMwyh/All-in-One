import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
import game_functions


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion-1")
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	score_board = ScoreBoard(ai_settings, screen, stats)
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	game_functions.create_fleet(ai_settings, screen, ship, aliens)
	
	clock = pygame.time.Clock()
	# font = pygame.font.Font(None, 30)
	
	while True:
		clock.tick(ai_settings.ship_speed_factor * 300)
		game_functions.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			game_functions.update_bullets(ai_settings, screen, stats, score_board, ship, aliens, bullets)
			game_functions.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		game_functions.update_screen(ai_settings, screen, stats, score_board, ship, aliens, bullets, play_button)
		
		# fps = clock.get_fps()
		# fps_text = font.render("FPS: {:.2f}".format(fps), True, (255, 255, 255))
		# screen.blit(fps_text, (10, 10))
		#
		# pygame.display.flip()


run_game()
