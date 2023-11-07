import pygame
import sys

screen = pygame.display.set_mode((600, 1000))

rect = pygame.Rect(10, 10, 100, 100)

rect2 = pygame.Rect(11, 11, 99, 99)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill((60, 60, 60), rect)
	screen.fill((230, 230, 230), rect2)
	pygame.display.flip()