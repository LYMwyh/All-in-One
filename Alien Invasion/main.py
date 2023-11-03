import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions


def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	
	while True:
		game_functions.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		game_functions.update_bullets(bullets)
		game_functions.update_screen(ai_settings, screen, ship, bullets)


run_game()
