import pygame

class Ship():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load('images/rocket.png')
		self.rect = self.image.get_rect()  # rectangle
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		# block transfer == blit
		self.screen.blit(self.image, self.rect)
