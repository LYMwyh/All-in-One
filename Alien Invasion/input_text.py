import pygame.font


class InputText():
	def __init__(self, ai_settings, screen, x, y, width, height, hint):
		self.ai_settings = ai_settings
		self.screen = screen
		self.rect = pygame.Rect(x, y, width, height)
		self.hint = hint
		self.text = ""
		self.hint_color = (170, 170, 170)
		self.text_color = (30, 30, 30)
		
		self.letters_writing = None
		self.writing = False
		
		self.font = pygame.font.SysFont(None, 48)
		self.prep_hint(hint)
		self.text_size = len(hint)
		self.draw_input_text()
	
	def handle_event(self, event, stats):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				stats.username_start_input = not stats.username_start_input
			else:
				stats.username_start_input = False
				self.draw_input_text()
		elif event.type == pygame.KEYDOWN:
			if stats.username_start_input:
				self.writing = True
				if event.type == pygame.K_RETURN:
					self.text += "\n"
				elif event.type == pygame.K_BACKSPACE:
					self.text = self.text[:-1]
					self.text_size -= 1
				else:
					self.text += event.unicode
					self.text_size += 1
					self.letters_writing = event.unicode
				self.text = self.text.strip()
				self.text_image = self.font.render(self.text, True, self.text_color, self.ai_settings.input_text_bg_color)
				
		elif event.type == pygame.KEYUP:
			if stats.username_start_input:
				self.writing = False
				self.letters_writing = None
		
	def prep_hint(self, hint):
		self.hint_image = self.font.render(hint, True, self.hint_color, self.ai_settings.input_text_bg_color)

	def draw_input_text(self):
		self.screen.fill(self.ai_settings.input_text_bg_color, self.rect)
		if self.text_size == 0 and self.writing is False:
			self.screen.blit(self.hint_image, self.rect)
		else:
			self.screen.blit(self.text_image, self.rect)
		
		