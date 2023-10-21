import tkinter.font
from tkinter import *
import random
import time
import algorithm

root = Tk()
root.title("Twenty Four")
root.geometry("800x400+100+100")

size = 14

print_frame_border = Frame(root, bg="white", bd=1)
print_text = Text(print_frame_border, bg="black", fg="white", font=('Arial', size))

input_frame_border = Frame(root, bg="white", bd=1)
input_frame = Frame(input_frame_border, bg="black")
button_close = Button(input_frame, text="closed", font=('Arial', size), command=root.quit)

button_yes = Button(input_frame, text="YES", font=size)
button_no = Button(input_frame, text="NO", font=size)

input_frame_hint = Label(input_frame, text="Input Frame", bg="black", fg="white", font=('Arial', size))
input_text = Text(input_frame, bg="black", fg="white", font=('Arial', size))

fonts = tkinter.font.families()
font = ""


def open_font_window():
	global fonts, font
	font_window = Toplevel(root)
	font_box = Frame(font_window, bg="black", bd=1)
	font_box.place(relx=0, rely=0, relwidth=1, relheight=0.8)
	var = StringVar(value="")
	font_label = Label(font_window, textvariable=var)
	font_label.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)
	
	def update_font_name():
		global font
		font = var.get()
	
	confirm = Button(font_window, text="Confirm", command=lambda: update_font_name())
	confirm.place(relx=0, rely=0.9, relwidth=1, relheigth=0.1)
	font_buttons = []
	for font_name in fonts:
		font_button = Radiobutton(font_box, text=font_name, variable=var, value=font_name, fg="white")
		font_button.configure(command=lambda: font_label.configure(text=var.get()))
		font_button.pack()
		font_buttons.append(font_button)


def add_or_reduce_font_size(yes):
	global size
	if yes:
		size += 1
	else:
		size -= 1
	if print_text['state'] == DISABLED:
		print_text.configure(state=NORMAL)
		print_text.configure(font=('Arial', size))
		print_text.configure(state=DISABLED)
	else:
		print_text.configure(font=('Arial', size))
	if button_yes['state'] == DISABLED:
		button_yes.configure(state=NORMAL)
		button_yes.configure(font=('Arial', size))
		button_yes.configure(state=DISABLED)
	else:
		button_yes.configure(font=('Arial', size))
	if button_no['state'] == DISABLED:
		button_no.configure(state=NORMAL)
		button_no.configure(font=('Arial', size))
		button_no.configure(state=DISABLED)
	else:
		button_no.configure(font=('Arial', size))
	
	if increase_font_size['state'] == DISABLED:
		increase_font_size.configure(state=NORMAL)
		increase_font_size.configure(font=('Arial', size))
		increase_font_size.configure(state=DISABLED)
	else:
		increase_font_size.configure(font=('Arial', size))
	if decrease_font_size['state'] == DISABLED:
		decrease_font_size.configure(state=NORMAL)
		decrease_font_size.configure(font=('Arial', size))
		decrease_font_size.configure(state=DISABLED)
	else:
		decrease_font_size.configure(font=('Arial', size))
	if button_close['state'] == DISABLED:
		button_close.configure(state=NORMAL)
		button_close.configure(font=('Arial', size))
		button_close.configure(state=DISABLED)
	else:
		button_close.configure(font=('Arial', size))
	if input_frame_hint['state'] == DISABLED:
		input_frame_hint.configure(state=NORMAL)
		input_frame_hint.configure(font=('Arial', size))
		input_frame_hint.configure(state=DISABLED)
	else:
		input_frame_hint.configure(font=('Arial', size))
	if input_text['state'] == DISABLED:
		input_text.configure(state=NORMAL)
		input_text.configure(font=('Arial', size))
		input_text.configure(state=DISABLED)
	else:
		input_text.configure(font=('Arial', size))
	if submit['state'] == DISABLED:
		submit.configure(state=NORMAL)
		submit.configure(font=('Arial', size))
		submit.configure(font=DISABLED)
	else:
		submit.configure(font=('Arial', size))
	root.update()


increase_font_size = Button(input_frame_border, text="font size +", command=lambda: add_or_reduce_font_size(True),
                            font=('Arial', size))
decrease_font_size = Button(input_frame_border, text="font size -", command=lambda: add_or_reduce_font_size(False),
                            font=('Arial', size))


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
	print_frame_border.place(relx=0, rely=0, relwidth=0.5, relheight=1)
	print_text.place(x=0, y=0, relwidth=1, relheight=1)
	input_frame_border.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
	input_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
	increase_font_size.place(relx=0, rely=0, relwidth=1, relheight=0.1)
	decrease_font_size.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
	input_frame_hint.place(relx=0.5, rely=0.5, anchor='center')
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


def identify_font():
	pass


def select_font():
	Start.place_forget()
	Start.configure(command=lambda: identify_font())
	Start.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


Start = Button(root, text="Start", command=lambda: select_font(), font=('Arial', size))
Start.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
