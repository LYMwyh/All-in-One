import pygame.font


class InputText():
	def __init__(self, ai_settings, screen, hint=""):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		
		self.rect = pygame.Rect(0, 0, 0, 0)
		
		self.hint = hint
		self.text = ""
		self.hint_color = (170, 170, 170)
		self.text_color = (255, 255, 255)
		
		self.writing = False
		
		self.font = pygame.font.SysFont(None, 48)
		
		self.draw_input_text()
	
	def prep_image(self):
		self.hint_image = self.font.render(self.hint, True, self.hint_color, self.ai_settings.input_text_bg_color)
		self.text_image = self.font.render(self.text, True, self.text_color, self.ai_settings.input_text_bg_color)
	
	def draw_input_text(self):
		self.prep_image()
		self.update_size()
		self.screen.fill(self.ai_settings.input_text_bg_color, self.rect)
		if len(self.text) == 0 and self.writing is False:
			self.screen.blit(self.hint_image, self.rect)
		else:
			self.screen.blit(self.text_image, self.rect)
	
	def update_size(self):
		if len(self.text):
			self.rect.w = max(200, self.text_image.get_width())
			self.rect.h = self.text_image.get_height()
		else:
			self.rect.w = max(200, self.hint_image.get_width())
			self.rect.h = self.hint_image.get_height()
		self.rect.center = self.screen_rect.center
		
		