from label import Label
import copy


def username_confirm_button_prep(username_confirm, username_input_text):
	username_confirm.rect.centerx = username_confirm.screen_rect.centerx
	username_confirm.rect.top = username_input_text.rect.bottom + 10
	username_confirm.msg_image_rect.center = username_confirm.rect.center


def play_button_prep(play_button):
	play_button.rect.center = play_button.screen_rect.center
	play_button.msg_image_rect.center = play_button.rect.center


def introduction_of_game_prep(ai_settings, screen, introduction_of_game):
	introduction_of_game.append(
		"This game called Alien Invasion.\n"
		"You need to fire at the UFOs "
		"and try not to let them reach the bottom line of the screen or touch you.\n"
		"If this happens, you will die.\n"
		"You will have 3 lives each time.")
	introduction_of_game.append(
		"The first number in the upper left corner of the screen indicates you highest score.\n"
		"The second number represents the score you got this time.\n"
		"The third number represents your level. Every time you kill a UFO swarm, your level increases by one.\n"
		"Finally is your username.")
	introduction_of_game.append(
		"There is a number in the top center of the screen that represents the highest score among all users.\n"
		"If there is a highest score, on the second line is the name of the user who achieved that score.\n"
		"If there is no high score, the high score will be displayed as 0 and the second line will not appear.")
	for page_ordinal, page in enumerate(copy.copy(introduction_of_game)):
		introduction_of_game[page_ordinal] = Label(ai_settings, screen, introduction_of_game[page_ordinal])


def next_button_prep(next_button, introduction_of_group):
	next_button.rect.centerx = next_button.screen_rect.centerx
	next_button.rect.top = introduction_of_group[-1].text_list[-1][1].bottom + 10
	next_button.msg_image_rect.center = next_button.rect.center


def back_button_prep(back_button, next_button):
	back_button.rect.centerx = back_button.screen_rect.centerx
	back_button.rect.top = next_button.rect.bottom + 10
	back_button.msg_image_rect.center = back_button.rect.center