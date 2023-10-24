import tkinter.font
from tkinter import *
import random
import time
import algorithm

root = Tk()
root.title("Twenty Four")
root.geometry("800x400+100+100")

Start = Button(root, text="Start")

setting = Button(root, text="Setting")

print_frame_border = Frame(root, bg="white", bd=1)
print_text = Text(print_frame_border, bg="black", fg="white")

input_frame_border = Frame(root, bg="white", bd=1)
input_frame = Frame(input_frame_border, bg="black")
input_text = Text(input_frame, bg="black", fg="white")

button_yes = Button(input_frame, text="YES")
button_no = Button(input_frame, text="NO")
button_close = Button(input_frame, text="closed", command=root.quit)

setting_content = [setting,
                   'setting_window',
                   print_text,
                   button_yes,
                   button_no,
                   input_text,
                   button_close]

setting_content_detail = {
	0: [setting, "Setting"],
	1: ['setting_window', 'setting_window'],
	2: [print_text, "Print Text"],
	3: [button_yes, "Button Yes"],
	4: [button_no, "Button No"],
	5: [input_text, "Input text"],
	6: [button_close, "Button Close"]
}

fonts = tkinter.font.families()

font_family = {}
for content_name in setting_content:
	font_family[content_name] = tkinter.font.Font(family=fonts[0], size=10)
	if type(content_name) != str:
		content_name.configure(font=font_family[content_name])


def open_setting_window():
	global font_family, setting_content_detail, setting_content
	setting_window = Toplevel(root)
	
	setting_frame = {}
	for content_name in setting_content:
		setting_frame[content_name] = Frame(setting_window)
	
	setting_menu_button = {}
	font_style_vars = []
	for detail in setting_content_detail.values():
		font_style_vars.append(StringVar(setting_frame[detail[0]]))
		font_style_vars[-1].set(font_family[detail[0]]['family'])
		setting_menu_button[detail[0]] = Menubutton(setting_frame[detail[0]],
		                                            font=(font_family[detail[0]]['family'], 13),
		                                            textvariable=font_style_vars[-1])
	
	def update_font_print(widget, **kwargs):
		if 'font_style' in kwargs:
			font_style = kwargs['font_style']
			font_family[widget]['family'] = font_style
			setting_menu_button[widget].configure(text=font_style, font=(font_style, 13))
		if 'font_size' in kwargs:
			font_size = setting_entry[widget].get()
			if font_size != "":
				font_family[widget]['size'] = int(font_size)
		
		if widget['state'] == DISABLED:
			widget.configure(state=NORMAL)
			widget.configure(font=font_family[widget])
			widget.configure(state=DISABLED)
		else:
			widget.configure(font=font_family[widget])
	
	setting_menu = {}
	for i, (key_value, element) in enumerate(setting_menu_button.items()):
		setting_menu[key_value] = Menu(element, tearoff=0)
		setting_menu_button[key_value].configure(menu=setting_menu[key_value])
		if key_value == "setting_window":
			continue
		for each_font in fonts:
			setting_menu[key_value].add_radiobutton(label=each_font, font=(each_font, 13), variable=font_style_vars[i],
			                                        command=lambda widget=key_value,
			                                                       new_font=each_font: update_font_print(widget,
			                                                                                             font_style=new_font))
	
	def on_focus_out(entry, widget):
		entry.delete(0, 'end')
		entry.insert('end', str(font_family[widget]['size']))
	
	def only_int_input(P):
		if P.isdigit():
			return True
		elif P == "":
			return True
		else:
			return False
	
	setting_entry = {}
	setting_entry_button = {}
	for key, detail in setting_content_detail.items():
		setting_entry[detail[0]] = Entry(setting_frame[detail[0]], validate="key", validatecommand=(setting_window.register(only_int_input), '%P'))
		setting_entry[detail[0]].insert('end', str(font_family[detail[0]]['size']))
		setting_entry[detail[0]].bind('<FocusOut>', lambda event, entry=setting_entry[detail[0]], widget=detail[0]: on_focus_out(entry, widget))
		setting_entry_button[detail[0]] = Button(setting_frame[detail[0]], text="Confirm")
		setting_entry_button[detail[0]].config(command=lambda widget=detail[0], new_size=True: update_font_print(widget, font_size=new_size))
	
	setting_widget_hint = {}
	for key, element in setting_content_detail.items():
		setting_widget_hint[element[0]] = []
		if element[0] == 'setting_window':
			continue
		setting_widget_hint[element[0]].append(
			Label(setting_frame[element[0]], text=element[1], font=font_family['setting_window']))
		setting_widget_hint[element[0]].append(
			Label(setting_frame[element[0]], text=element[1] + ' font style: ', font=font_family['setting_window']))
		setting_widget_hint[element[0]].append(
			Label(setting_frame[element[0]], text=element[1] + ' size: ', font=font_family['setting_window']))
	
	def update_font_in_setting_window(**kwargs):
		global font_family
		if 'update_font_style' in kwargs:
			font_style = kwargs['update_font_style']
			font_family['setting_window']['family'] = font_style
			setting_menu_button['setting_window'].configure(text=font_style, font=(font_style, 13))
		if 'add_size' in kwargs and kwargs['add_size']:
			font_family['setting_window']['size'] += 1
		if 'subtract_size' in kwargs and kwargs['subtract_size']:
			font_family['setting_window']['size'] -= 1
		size_add.configure(font=font_family['setting_window'])
		size_subtract.configure(font=font_family['setting_window'])
		for ordinal_number in range(7):
			if ordinal_number == 1:
				continue
			setting_widget_hint[setting_content_detail[ordinal_number][0]][0].config(font=font_family['setting_window'])
			setting_widget_hint[setting_content_detail[ordinal_number][0]][1].config(font=font_family['setting_window'])
			setting_widget_hint[setting_content_detail[ordinal_number][0]][2].config(font=font_family['setting_window'])
	
	# 开始放置
	for each_font in fonts:
		setting_menu['setting_window'].add_radiobutton(label=each_font, font=(each_font, 13),
		                                               variable=font_style_vars[1],
		                                               command=lambda new_font=each_font: update_font_in_setting_window(
			                                               update_font_style=new_font))
		
	setting_menu_button['setting_window'].pack(fill='x', side='top', expand=True)
	
	size_add = Button(setting_frame['setting_window'], text="font size +",
	                  command=lambda: update_font_in_setting_window(add_size=True))
	size_add.configure(font=font_family['setting_window'])
	size_subtract = Button(setting_frame['setting_window'], text="font size -",
	                       command=lambda: update_font_in_setting_window(subtract_size=True))
	size_subtract.configure(font=font_family['setting_window'])
	
	size_add.pack(fill='x', side='left', expand=True)
	size_subtract.pack(fill='x', side='right', anchor="center", expand=True)
	setting_frame['setting_window'].pack(fill='x')
	
	def draw_line(canvas):
		canvas.delete('all')
		canvas.create_line(0, 0, canvas.winfo_width(), 0, width=canvas.winfo_height(), fill='black')
	
	dividing_line = []
	for ordinal_number in range(8):
		if ordinal_number == 1:
			continue
		dividing_line.append(Canvas(setting_window, height=1))
		dividing_line[-1].pack(fill='x')
		dividing_line[-1].bind("<Configure>", lambda event, canvas=dividing_line[-1]: draw_line(canvas))
		if ordinal_number == 7:
			break
		setting_widget_hint[setting_content_detail[ordinal_number][0]][0].grid(row=0, column=0)
		setting_widget_hint[setting_content_detail[ordinal_number][0]][1].grid(row=1, column=0)
		setting_menu_button[setting_content_detail[ordinal_number][0]].grid(row=1, column=1)
		setting_widget_hint[setting_content_detail[ordinal_number][0]][2].grid(row=2, column=0)
		setting_entry[setting_content_detail[ordinal_number][0]].grid(row=2, column=1)
		setting_entry_button[setting_content_detail[ordinal_number][0]].grid(row=2, column=2)
		setting_frame[setting_content_detail[ordinal_number][0]].pack(anchor='center')
	close = Button(setting_window, text="Closed", font=font_family['setting_window'], command=setting_window.destroy)
	close.pack(anchor='center')


setting.configure(command=lambda: open_setting_window())


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
	print_text.configure(state=NORMAL)
	printer("Do you want to know the whole answer(s)?")
	print_text.configure(state=DISABLED)
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
	
	print_text.configure(state=DISABLED)
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_yes():
	button_yes.place_forget()
	button_no.place_forget()
	
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
	
	print_text.configure(state=DISABLED)
	
	button_yes.configure(command=lambda: check_answer(True))
	button_no.configure(command=lambda: check_answer(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


def clicked_no():
	button_yes.place_forget()
	button_no.place_forget()
	
	print_text.configure(state=NORMAL)
	printer('\n')
	printer("OK!")
	printer("See you next time!")
	print_text.configure(state=DISABLED)
	
	button_close.place(relx=0, rely=0, relwidth=1, relheight=1)


def start():
	Start.place_forget()
	print_frame_border.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)
	print_text.place(relx=0, rely=0, relwidth=1, relheight=1)
	input_frame_border.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
	input_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
	setting.place(relx=0, rely=0, relwidth=1, relheight=0.1)
	printer("Here is a game:")
	printer("There will have four random numbers from 1 to 13, you need to use these four numbers calculate 24.")
	printer("Each number must and can only be used once.")
	printer("Sometimes, there is no solutions for figuring out 24.")
	printer("\n")
	
	printer("Do you want to play it with me?")
	print_text.configure(state=DISABLED)
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)


Start.configure(command=lambda: start())
Start.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
