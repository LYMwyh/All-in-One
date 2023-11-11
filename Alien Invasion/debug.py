
#
# def run_game():
#
#
#
# 	while True:
#
# 		#
# 		pygame.display.flip()
#
#
# run_game()


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
import sys


def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	#
	stats = GameStats(ai_settings)
	#
	introduction_of_game = []
	preprocessing.introduction_of_game_prep(ai_settings, screen, introduction_of_game)
	# 开始游戏的主循环
	while True:
		screen.fill(ai_settings.bg_color)
		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
		introduction_of_game[0].show_label()
		# 让最近绘制的屏幕可见
		pygame.display.flip()


run_game()