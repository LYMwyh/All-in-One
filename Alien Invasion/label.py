import pygame


class Label():
	def __init__(self, ai_settings, screen, text):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.text = text
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		self.format_content()
	
	
	def format_content(self):
		text_list = self.text.split('\n')
		self.text_list = []
		for ordinal_line, content in enumerate(text_list):
			text_image, text_image_rect = self.prep_content(text_list[ordinal_line])
			if ordinal_line == 0:
				text_image_rect.y = (self.screen_rect.h - text_image_rect.h * len(text_list))/2
			else:
				text_image_rect.top = self.text_list[ordinal_line - 1][1].bottom
			self.text_list.append([text_image, text_image_rect])
	
	
	def prep_content(self, text):
		text_image = self.font.render(text, True, self.text_color, self.ai_settings.bg_color)
		
		text_image_rect = text_image.get_rect()
		text_image_rect.centerx = self.screen_rect.centerx
		return text_image, text_image_rect
	
	def show_label(self):
		for each_text_line in self.text_list:
			text_image, text_image_rect = each_text_line
			self.screen.blit(text_image, text_image_rect)
