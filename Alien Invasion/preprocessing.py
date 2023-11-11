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
		"You need to fire at the UFOs \n "
		"and try not to let them reach \n"
		"the bottom line of the screen \n"
		"or touch you.\n"
		"If this happens, you will die.\n"
		"You will have 3 lives each time.")
	introduction_of_game.append(
		"The first number in the upper \n"
		"left corner of the screen indicates \n"
		" you highest score.\n"
		"The second number represents \n"
		" the score you got this time.\n"
		"The third number represents  \n"
		"your level. Every time you kill \n"
		"a UFO swarm, your level increases \n"
		"by one.\n"
		"Finally is your username.")
	introduction_of_game.append(
		"There is a number in the top \n"
		"center of the screen that  \n"
		"represents the highest score \n"
		"among all users.\n"
		"If there is a highest score, \n"
		"on the second line is the name \n"
		"of the user who achieved that score.\n"
		"If there is no high score, the \n"
		"high score will be displayed as \n"
		"0 and the second line will not appear.")
	for page_ordinal, page in enumerate(copy.copy(introduction_of_game)):
		introduction_of_game[page_ordinal] = Label(ai_settings, screen, introduction_of_game[page_ordinal])


def next_button_prep(next_button, stats, introduction_of_group):
	next_button.rect.centerx = next_button.screen_rect.centerx
	next_button.rect.top = introduction_of_group[stats.introduction_page].text_list[-1][1].bottom + 10
	next_button.msg_image_rect.center = next_button.rect.center


def back_button_prep(back_button, next_button):
	back_button.rect.centerx = back_button.screen_rect.centerx
	back_button.rect.top = next_button.rect.bottom + 10
	back_button.msg_image_rect.center = back_button.rect.center