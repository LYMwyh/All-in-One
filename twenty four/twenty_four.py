import tkinter.font
from tkinter import *
import random
import time
import algorithm

root = Tk()
root.title("Twenty Four")
root.geometry("800x400+100+100")

size = 14
fonts = tkinter.font.families()
font = fonts[0]

print_frame_border = Frame(root, bg="white", bd=1)
print_text = Text(print_frame_border, bg="black", fg="white", font=(font, size))

input_frame_border = Frame(root, bg="white", bd=1)
input_frame = Frame(input_frame_border, bg="black")
button_close = Button(input_frame, text="closed", font=(font, size), command=root.quit)

button_yes = Button(input_frame, text="YES", font=(font, size))
button_no = Button(input_frame, text="NO", font=(font, size))

input_frame_hint = Label(input_frame, text="Input Frame", bg="black", fg="white", font=(font, size))
input_text = Text(input_frame, bg="black", fg="white", font=(font, size))

setting = Button(root, text="Setting")
size_in_setting_window = 10
font_in_setting_window = fonts[0]


def open_setting_window():
	global font, size, font_in_setting_window, size_in_setting_window
	setting_window = Toplevel(root)
	
	font_menu_button = Menubutton(setting_window, text="Font")
	font_menu = Menu()
	for each_font in fonts:
		font_menu.add_command(label=each_font, font=(each_font, size))
	font_menu_button.configure(menu=font_menu)
	
	
	def update_font_in_setting_window(add):
		global size_in_setting_window
		if add:
			size_in_setting_window += 1
		else:
			size_in_setting_window -= 1
	
	size_add = Button(setting_window, text="font size +", command=lambda: update_font_in_setting_window(True), height=1)
	size_subtract = Button(setting_window, text="font size -", command=lambda: update_font_in_setting_window(False), height=1)
	
	size_add.master = setting_window
	size_subtract.master = setting_window
	size_add.place(relx=0, rely=0, relwidth=0.5)
	size_subtract.place(relx=0.5, rely=0, relwidth=0.5)
	
	label = Label(setting_window, text="Hello", font=(font_in_setting_window, size_in_setting_window))
	label.place(relx=)

setting.configure(command=lambda: open_setting_window())

def update_font_style_and_font_size(**kwargs):
	global size, font
	if kwargs['font_style']:
		font = kwargs['font_style']
	if kwargs['font_size_add']:
		size += 1
	elif kwargs['font_size_subtract']:
		size -= 1
	if print_text['state'] == DISABLED:
		print_text.configure(state=NORMAL)
		print_text.configure(font=(font, size))
		print_text.configure(state=DISABLED)
	else:
		print_text.configure(font=(font, size))
	if button_yes['state'] == DISABLED:
		button_yes.configure(state=NORMAL)
		button_yes.configure(font=(font, size))
		button_yes.configure(state=DISABLED)
	else:
		button_yes.configure(font=(font, size))
	if button_no['state'] == DISABLED:
		button_no.configure(state=NORMAL)
		button_no.configure(font=(font, size))
		button_no.configure(state=DISABLED)
	else:
		button_no.configure(font=(font, size))
	
	if increase_font_size['state'] == DISABLED:
		increase_font_size.configure(state=NORMAL)
		increase_font_size.configure(font=(font, size))
		increase_font_size.configure(state=DISABLED)
	else:
		increase_font_size.configure(font=(font, size))
	if decrease_font_size['state'] == DISABLED:
		decrease_font_size.configure(state=NORMAL)
		decrease_font_size.configure(font=(font, size))
		decrease_font_size.configure(state=DISABLED)
	else:
		decrease_font_size.configure(font=(font, size))
	if button_close['state'] == DISABLED:
		button_close.configure(state=NORMAL)
		button_close.configure(font=(font, size))
		button_close.configure(state=DISABLED)
	else:
		button_close.configure(font=(font, size))
	if input_frame_hint['state'] == DISABLED:
		input_frame_hint.configure(state=NORMAL)
		input_frame_hint.configure(font=(font, size))
		input_frame_hint.configure(state=DISABLED)
	else:
		input_frame_hint.configure(font=(font, size))
	if input_text['state'] == DISABLED:
		input_text.configure(state=NORMAL)
		input_text.configure(font=(font, size))
		input_text.configure(state=DISABLED)
	else:
		input_text.configure(font=(font, size))
	if submit['state'] == DISABLED:
		submit.configure(state=NORMAL)
		submit.configure(font=(font, size))
		submit.configure(font=DISABLED)
	else:
		submit.configure(font=(font, size))
	root.update()


increase_font_size = Button(root, text="font size +", command=lambda: update_font_style_and_font_size(font_style=False, font_size_add=True, font_size_subtract=False), font=(font, size))
decrease_font_size = Button(root, text="font size -", command=lambda: update_font_style_and_font_size(font_style=False, font_size_add=None, font_size_subtract=True), font=(font, size))


def printer(content, text=print_text):
	for char in content:
		text.insert('end', char)
		root.update()
		time.sleep(0)
	text.insert('end', '\n')


def whether_know_whole_answer():
	input_text.place_forget()
	button_yes.place_forget()
	button_yes.configure(text="YES")
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	print_text.configure(state=NORMAL)
	printer("Do you want to know the whole answer(s)?")
	print_text.configure(state=DISABLED)
	input_frame_hint.place_forget()
	button_yes.configure(command=lambda: whole_answers(True))
	button_no.configure(command=lambda: whole_answers(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def submit_answers():
	submit.configure(state=DISABLED)
	input_text.configure(state=DISABLED)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	answers = input_text.get('2.0', 'end')
	answers = answers.split('\n')
	answers.pop()
	# print(Whole_Answers)
	for answer_in_str in answers:
		num = False
		answer = []
		for char in answer_in_str:
			try:
				temporary_num = int(char)
				if num:
					answer[-1] *= 10
					answer[-1] += temporary_num
				else:
					num = True
					answer.append(temporary_num)
			except ValueError:
				num = False
				answer.append(char)
		for step in range(len(answer)):
			if type(answer[step]) is int:
				answer[step] = float(answer[step])
		algorithm.simplify_formula_first_part(answer)
		answer, temporary_num = algorithm.simplify_formula_second_part(0, answer)
		for step in range(len(answer)):
			if type(answer[step]) is float:
				answer[step] = int(answer[step])
		answer = ''.join(list(map(str, answer)))
		# print(answer)
		if answer in algorithm.Whole_Answers:
			printer("True")
		else:
			printer("False")
	print_text.configure(state=DISABLED)
	submit.place_forget()
	button_yes.configure(text="Next")
	button_yes.configure(command=lambda: whether_know_whole_answer())
	button_yes.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


submit = Button(input_frame, text="Submit", command=lambda: submit_answers())


def check_answer(yes):
	button_yes.place_forget()
	button_no.place_forget()
	
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	
	print_text.configure(state=NORMAL)
	printer("OK!")
	time.sleep(1.0)
	print_text.delete('1.0', 'end')
	if yes is True:
		printer(
			"Four numbers: %d , %d , %d , %d ." % (
				algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2],
				algorithm.Four_Numbers[3]))
		printer("Please input your answer(s) in the input frame.")
		printer("Each line write one answer.You don't need to write '=24' in the end.")
		print_text.configure(state=DISABLED)
		
		input_frame_hint.place_forget()
		
		input_text.configure(state=NORMAL)
		input_text.delete('1.0', 'end')
		input_text.place(relx=0, rely=0, relwidth=1, relheight=0.9)
		submit.configure(state=NORMAL)
		submit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
		printer("Example: a+b+c+d", input_text)
	else:
		whether_know_whole_answer()


def whole_answers(yes):
	button_yes.place_forget()
	button_no.place_forget()
	
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	
	print_text.configure(state=NORMAL)
	printer('\n')
	printer("OK!")
	time.sleep(1.0)
	print_text.delete('1.0', 'end')
	if yes is True:
		if len(algorithm.Whole_Answers) == 0:
			printer("There is no any answers!")
		else:
			for Each_Answer in algorithm.Whole_Answers:
				printer(Each_Answer + "=24")
	printer("Do you want to play it again?")
	
	input_frame_hint.place_forget()
	
	print_text.configure(state=DISABLED)
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_yes():
	button_yes.place_forget()
	button_no.place_forget()
	
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	
	algorithm.Whole_Answers = []
	algorithm.the_Selected_Operators = []
	algorithm.Four_Numbers = []
	for _ in range(4):
		algorithm.Four_Numbers.append(float(random.randint(1, 13)))
	
	print_text.configure(state=NORMAL)
	printer('\n')
	printer('OK!')
	time.sleep(0.2)
	print_text.delete('1.0', 'end')
	printer("Here is four numbers: %d , %d , %d , %d ." % (
		algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2], algorithm.Four_Numbers[3]))
	time.sleep(1)
	
	algorithm.calculate_the_whole_answers()
	
	printer("Did you find the answer(s)?")
	printer("If yes, do you want to check your answer(s)?")
	
	input_frame_hint.place_forget()
	print_text.configure(state=DISABLED)
	
	button_yes.configure(command=lambda: check_answer(True))
	button_no.configure(command=lambda: check_answer(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_no():
	button_yes.place_forget()
	button_no.place_forget()
	
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	
	print_text.configure(state=NORMAL)
	printer('\n')
	printer("OK!")
	printer("See you next time!")
	print_text.configure(state=DISABLED)
	
	input_frame_hint.place_forget()
	button_close.place(relx=0, rely=0, relwidth=1, relheight=1)


def start():
	Start.place_forget()
	print_frame_border.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)
	print_text.place(relx=0, rely=0, relwidth=1, relheight=1)
	input_frame_border.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
	input_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
	setting.place(relx=0, rely=0, relwidth=1, relheight=0.1)
	printer("Here is a game:")
	printer("There will have four random numbers from 1 to 13, you need to use these four numbers calculate 24.")
	printer("Each number must and can only be used once.")
	printer("Sometimes, there is no solutions for figuring out 24.")
	printer("\n")
	
	printer("Do you want to play it with me?")
	print_text.configure(state=DISABLED)
	input_frame_hint.place_forget()
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


Start = Button(root, text="Start", command=lambda: start(), font=('Arial', size))
Start.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
