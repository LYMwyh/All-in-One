import tkinter.font
from tkinter import *
import random
import time
import algorithm
import platform
import datetime

root = Tk()
root.title("Twenty Four")
root.geometry("800x400+100+100")

Start = Button(root, text="Start")

setting = Button(root, text="Setting")

print_frame_border = Frame(root, bg="white", bd=1)
print_text = Text(print_frame_border, bg="black", fg="white", wrap="word")

input_frame_border = Frame(root, bg="white", bd=1)
input_frame = Frame(input_frame_border, bg="black")
example = Text(input_frame, bg="black", fg="white")
input_text = Text(input_frame, bg="black", fg="white", insertbackground='white')
submit = Button(input_frame, text="Submit")

button_next = Button(input_frame, text="Next")
button_yes = Button(input_frame, text="YES")
button_no = Button(input_frame, text="NO")
button_close = Button(input_frame, text="closed", command=root.quit)

button_game_mode = Button(root, text="Game Mode")

button_again = Button(input_frame, text="Again")

button_answer_mode = Button(root, text="Answer Mode")

mode = 0

state_of_change_mode = StringVar()
state_of_change_mode.set('normal')

setting_content = [setting,
                   'setting_window',
                   print_text,
                   button_yes,
                   button_no,
                   example,
                   input_text,
                   submit,
                   button_next,
                   button_close,
                   button_again,
                   button_game_mode,
                   button_answer_mode]

setting_content_detail = {
	setting: ["Setting", True, True, False],
	'setting_window': ['setting_window', True, True, True],
	print_text: ["Print Text", True, True, False],
	button_yes: ["Button Yes", True, False, False],
	button_no: ["Button No", True, False, False],
	example: ["Example", True, True, False],
	input_text: ["Input text", True, True, False],
	submit: ["Submit", True, True, False],
	button_next: ["Button Next", True, True, False],
	button_close: ["Button Close", True, True, False],
	button_again: ["Button Again", False, True, False],
	button_game_mode: ["Button Game Mode", False, False, True],
	button_answer_mode: ["Button Answer Mode", False, False, True]
}

fonts = tkinter.font.families()

font_family = {}
for content_name in setting_content:
	font_family[content_name] = tkinter.font.Font(family=fonts[0], size=13)
	if type(content_name) is not str:
		content_name.configure(font=font_family[content_name])


def open_setting_window():
	global font_family, setting_content_detail, setting_content, mode
	setting_window = Toplevel(root)
	setting_window.title("Twenty Four Setting Window")
	
	setting_window_top_frame = Frame(setting_window)
	setting_window_secondary_frame = Frame(setting_window_top_frame)
	setting_window_secondary_frame.pack(anchor='center', expand=True)
	setting_window_top_frame.pack(side='left', fill='both', expand=True)
	
	setting_window_canvas = Canvas(setting_window_secondary_frame)
	setting_window_canvas_scrollbar = Scrollbar(setting_window, orient="vertical", command=setting_window_canvas.yview)
	setting_window_canvas.pack(anchor='center', fill='both')
	setting_window_canvas_scrollbar.pack(side='right', fill='y')
	setting_window_frame = Frame(setting_window_canvas)
	
	setting_window_canvas.create_window((0, 0), window=setting_window_frame, anchor='center', tags='frame')
	
	def update_scroll_region_and_canvas_size(event):
		setting_window_canvas.configure(scrollregion=setting_window_canvas.bbox('all'))
		setting_window_canvas.configure(yscrollcommand=setting_window_canvas_scrollbar.set)
		setting_window_canvas.configure(width=setting_window_frame.winfo_width(),
		                                height=setting_window_frame.winfo_height())
	
	setting_window_frame.bind('<Configure>', update_scroll_region_and_canvas_size)
	
	def on_mousewheel(event):
		if platform.system() == 'Windows':
			setting_window_canvas.yview_scroll(int(-1 * event.delta / 120), 'units')
		elif platform.system() == 'Darwin':
			setting_window_canvas.yview_scroll(int(-1 * event.delta), 'units')
		else:
			if event.num == 4:
				setting_window_canvas.yview_scroll(-1, 'units')
			elif event.num == 5:
				setting_window_canvas.yview_scroll(1, 'units')
	
	if platform.system() == 'Windows' or platform.system() == 'Darwin':
		setting_window_canvas.bind_all("<MouseWheel>", on_mousewheel)
	else:
		setting_window_canvas.bind_all("<Button-4", on_mousewheel)
		setting_window_canvas.bind_all("<Button-5>", on_mousewheel)
	
	def change_widget_state(widget, use):
		if setting_window in root.winfo_children():
			if len(widget.winfo_children()) != 0:
				for children_widget in widget.winfo_children():
					change_widget_state(children_widget, use)
			if 'state' in widget.configure():
				if use:
					widget.configure(state=NORMAL)
				else:
					widget.configure(state=DISABLED)
	
	def on_enter(event, widget, frame):
		global setting_content_detail
		if widget.winfo_viewable():
			widget.configure(highlightbackground='red')
	
	def on_leave(event, widget):
		widget.configure(highlightbackground='systemWindowBackgroundColor')
	
	setting_frame = {}
	for content_name in setting_content:
		if setting_content_detail[content_name][mode] is True:
			setting_frame[content_name] = Frame(setting_window_frame)
			if content_name == 'setting_window':
				continue
			setting_frame[content_name].bind('<Enter>', lambda event, widget=content_name,
			                                                   frame=setting_frame[content_name]: on_enter(event,
			                                                                                               widget,
			                                                                                               frame))
			setting_frame[content_name].bind('<Leave>', lambda event, widget=content_name: on_leave(event, widget))
	
	def on_map(event, widget):
		change_widget_state(setting_frame[widget], True)
	
	def on_unmap(event, widget):
		change_widget_state(setting_frame[widget], False)
	
	for content_name in setting_content:
		if content_name == 'setting_window':
			continue
		if setting_content_detail[content_name][mode] is True:
			content_name.bind("<Map>", lambda event, widget=content_name: on_map(event, widget))
			content_name.bind("<Unmap>", lambda event, widget=content_name: on_unmap(event, widget))
	
	setting_menu_button = {}
	font_style_vars = []
	for content_name in setting_content:
		if setting_content_detail[content_name][mode] is True:
			font_style_vars.append(StringVar(setting_frame[content_name]))
			font_style_vars[-1].set(font_family[content_name]['family'])
			setting_menu_button[content_name] = Menubutton(setting_frame[content_name],
			                                               font=(font_family[content_name]['family'], 13),
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
		if 'add_size' in kwargs:
			font_family[widget]['size'] += 1
			setting_entry[widget].delete(0, 'end')
			setting_entry[widget].insert('end', str(font_family[widget]['size']))
		if 'subtract_size' in kwargs:
			font_family[widget]['size'] -= 1
			setting_entry[widget].delete(0, 'end')
			setting_entry[widget].insert('end', str(font_family[widget]['size']))
		
		if widget['state'] == DISABLED:
			widget.configure(state=NORMAL)
			widget.configure(font=font_family[widget])
			widget.configure(state=DISABLED)
		else:
			widget.configure(font=font_family[widget])
	
	setting_menu = {}
	for i, (key_value, element) in enumerate(setting_menu_button.items()):
		if setting_content_detail[key_value][mode] is True:
			setting_menu[key_value] = Menu(element, tearoff=0)
			setting_menu_button[key_value].configure(menu=setting_menu[key_value])
			if key_value == "setting_window":
				continue
			for each_font in fonts:
				setting_menu[key_value].add_radiobutton(label=each_font, font=(each_font, 13),
				                                        variable=font_style_vars[int(i)],
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
	for content_name in setting_content:
		if setting_content_detail[content_name][mode] is True:
			setting_entry[content_name] = Entry(setting_frame[content_name], validate="key",
			                                    validatecommand=(setting_window_frame.register(only_int_input), '%P'))
			setting_entry[content_name].insert('end', str(font_family[content_name]['size']))
			setting_entry[content_name].bind('<FocusOut>',
			                                 lambda event, entry=setting_entry[content_name],
			                                        widget=content_name: on_focus_out(
				                                 entry, widget))
			setting_entry_button[content_name] = Button(setting_frame[content_name], text="Confirm")
			setting_entry_button[content_name].config(
				command=lambda widget=content_name, new_size=True: update_font_print(widget, font_size=new_size))
	
	setting_font_size_frame = {}
	setting_font_size_button = {}
	# icon_up = PhotoImage(file="icon-up.png")
	# icon_down = PhotoImage(file="icon-down.png")
	for content_name in setting_content:
		if setting_content_detail[content_name][mode] is True:
			if content_name == 'setting_window':
				continue
			setting_font_size_frame[content_name] = Frame(setting_frame[content_name])
			setting_font_size_button[content_name] = []
			setting_font_size_button[content_name].append(Button(setting_font_size_frame[content_name], text='+',
			                                                     command=lambda widget=content_name: update_font_print(
				                                                     widget, add_size=True)))
			setting_font_size_button[content_name].append(Button(setting_font_size_frame[content_name], text='-',
			                                                     command=lambda widget=content_name: update_font_print(
				                                                     widget, subtract_size=True)))
	
	setting_widget_hint = {}
	for key, element in setting_content_detail.items():
		if element[mode] is True:
			setting_widget_hint[key] = []
			if key == 'setting_window':
				continue
			setting_widget_hint[key].append(
				Label(setting_frame[key], text=element[0], font=font_family['setting_window']))
			setting_widget_hint[key].append(
				Label(setting_frame[key], text=element[0] + ' font style: ', font=font_family['setting_window']))
			setting_widget_hint[key].append(
				Label(setting_frame[key], text=element[0] + ' size: ', font=font_family['setting_window']))
	
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
		for ordinal_number in range(len(setting_content)):
			if setting_content_detail[setting_content[ordinal_number]][mode] is True:
				if ordinal_number == 1:
					continue
				setting_widget_hint[setting_content[ordinal_number]][0].config(font=font_family['setting_window'])
				setting_widget_hint[setting_content[ordinal_number]][1].config(font=font_family['setting_window'])
				setting_widget_hint[setting_content[ordinal_number]][2].config(font=font_family['setting_window'])
	
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
	for ordinal_number in range(len(setting_content)):
		if setting_content_detail[setting_content[ordinal_number]][mode] is True:
			if ordinal_number == 1:
				continue
			dividing_line.append(Canvas(setting_window_frame, height=1))
			dividing_line[-1].pack(fill='x')
			dividing_line[-1].bind("<Configure>", lambda event, canvas=dividing_line[-1]: draw_line(canvas))
			if ordinal_number == len(setting_content):
				break
			setting_widget_hint[setting_content[ordinal_number]][0].grid(row=0, column=0)
			setting_widget_hint[setting_content[ordinal_number]][1].grid(row=1, column=0)
			setting_menu_button[setting_content[ordinal_number]].grid(row=1, column=1)
			setting_widget_hint[setting_content[ordinal_number]][2].grid(row=2, column=0)
			setting_entry[setting_content[ordinal_number]].grid(row=2, column=1)
			
			setting_font_size_button[setting_content[ordinal_number]][0].pack(side='top', fill='x', expand=True)
			setting_font_size_button[setting_content[ordinal_number]][1].pack(side='bottom', fill='x', expand=True)
			setting_font_size_frame[setting_content[ordinal_number]].grid(row=2, column=2)
			
			setting_entry_button[setting_content[ordinal_number]].grid(row=2, column=3)
			setting_frame[setting_content[ordinal_number]].pack(anchor='center')
	dividing_line.append(Canvas(setting_window_frame, height=1))
	dividing_line[-1].pack(fill='x')
	dividing_line[-1].bind("<Configure>", lambda event, canvas=dividing_line[-1]: draw_line(canvas))
	change_mode = Button(setting_window_frame, text="Change Mode", font=font_family['setting_window'],
	                     command=lambda: selected_mode())
	if mode != 3:
		change_mode.pack(side='left', fill='x', expand=True)
		if state_of_change_mode.get() == 'normal':
			change_mode.configure(state=NORMAL)
		else:
			change_mode.configure(state=DISABLED)
	close = Button(setting_window_frame, text="Closed", font=font_family['setting_window'],
	               command=setting_window.destroy)
	close.pack(side='right', fill='x', expand=True)
	
	for content_name in setting_content:
		if setting_content_detail[content_name][mode] is True:
			if content_name == 'setting_window':
				continue
			if content_name.winfo_viewable():
				change_widget_state(setting_frame[content_name], True)
			else:
				change_widget_state(setting_frame[content_name], False)
	
	def whether_could_change_mode(*args):
		if state_of_change_mode.get() == 'normal':
			if setting_window in root.winfo_children():
				change_mode.configure(state=NORMAL)
		else:
			if setting_window in root.winfo_children():
				change_mode.configure(state=DISABLED)
	
	state_of_change_mode.trace('w', whether_could_change_mode)


def close_root():
	hint_window = Toplevel(root)
	if state_of_change_mode.get() == 'normal':
		hint_text = Label(hint_window, text="Are you sure you want to end the game?")
		hint_text.pack(side='top', expand=True)
		button_yes_close = Button(hint_window, text="Yes", command=root.quit)
		button_no_close = Button(hint_window, text="Not sure", command=hint_window.destroy)
		button_yes_close.pack(side='left', expand=True)
		button_no_close.pack(side='right', expand=True)
	else:
		hint_text = Text(hint_window, height=1)
		hint_text.insert('end', "When content stops putting, you can close the window.")
		hint_text.configure(state=DISABLED)
		hint_text.pack()
		Label(hint_window, text=str(datetime.datetime.today()), fg='red').pack()


root.protocol("WM_DELETE_WINDOW", close_root)


def printer(content, text=print_text):
	for char in content:
		text.configure(state=NORMAL)
		text.insert('end', char)
		text.configure(state=DISABLED)
		root.update()
		time.sleep(0)
	text.configure(state=NORMAL)
	text.insert('end', '\n')
	text.configure(state=DISABLED)


def whether_want_to_know_whole_answer():
	state_of_change_mode.set('disable')
	example.place_forget()
	input_text.place_forget()
	button_next.place_forget()
	
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	
	printer("Do you want to know all the answers?")
	printer("Maybe there is no any answers.")
	
	button_yes.configure(command=lambda: whole_answers(True))
	button_no.configure(command=lambda: whole_answers(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
	state_of_change_mode.set('normal')


def submit_answers():
	state_of_change_mode.set('disable')
	submit.configure(state=DISABLED)
	input_text.configure(state=DISABLED)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	answers = input_text.get('1.0', 'end')
	answers = answers.split('\n')
	answers.pop()
	# print(Whole_Answers)
	for answer_in_str in answers:
		num = False
		answer = []
		if len(answer_in_str) == 0:
			continue
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
		if not algorithm.check_format(answer):
			printer("Your answer's format can not be calculated!")
			continue
		algorithm.simplify_formula_first_part(answer)
		answer, temporary_num = algorithm.simplify_formula_second_part(0, answer, 0)
		answer = ''.join(list(map(str, answer)))
		# print(answer)
		if answer in algorithm.Whole_Answers:
			printer("True")
		else:
			printer("False")
	
	if answers == ['']:
		printer("You did not input any answers!")
	submit.place_forget()
	button_next.configure(command=lambda: whether_want_to_know_whole_answer())
	button_next.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
	state_of_change_mode.set('normal')


def check_answer(yes):
	state_of_change_mode.set('disable')
	button_yes.place_forget()
	button_no.place_forget()
	
	printer("OK!")
	time.sleep(1.0)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	if yes is True:
		printer(
			"Four numbers: %d , %d , %d , %d ." % (
				algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2],
				algorithm.Four_Numbers[3]))
		printer("Please input your answer(s) in the input frame.")
		printer("Each line writes one answer.You don't need to write '=24' in the end of each line.")
		
		example.configure(state=NORMAL)
		example.delete('1.0', 'end')
		example.configure(state=DISABLED)
		example.place(relx=0, rely=0, relwidth=1, relheight=0.1)
		input_text.configure(state=NORMAL)
		input_text.delete('1.0', 'end')
		input_text.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
		submit.configure(command=lambda: submit_answers())
		submit.configure(state=NORMAL)
		submit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
		printer("Example: a+b+c+d", example)
		state_of_change_mode.set('normal')
	else:
		whether_want_to_know_whole_answer()


def whole_answers(yes):
	state_of_change_mode.set('disable')
	button_yes.place_forget()
	button_no.place_forget()
	
	printer('\n')
	printer("OK!")
	time.sleep(1.0)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	if yes is True:
		if len(algorithm.Whole_Answers) == 0:
			printer("There is no any answers!")
		else:
			for Each_Answer in algorithm.Whole_Answers:
				printer(Each_Answer + "=24")
	printer("Do you want to play it again?")
	
	button_yes.configure(command=lambda: clicked_yes())
	button_no.configure(command=lambda: clicked_no())
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
	
	state_of_change_mode.set('normal')


def whether_have_answers(yes):
	state_of_change_mode.set('disable')
	printer("OK!")
	if yes:
		button_yes.configure(command=lambda: check_answer(True))
		button_no.configure(command=lambda: check_answer(False))
		printer("Did you find any answers?")
	else:
		time.sleep(1.0)
		whether_want_to_know_whole_answer()
	
	state_of_change_mode.set('normal')


def clicked_yes():
	state_of_change_mode.set('disable')
	button_yes.place_forget()
	button_no.place_forget()
	
	algorithm.Whole_Answers = []
	algorithm.the_Selected_Operators = []
	algorithm.Four_Numbers = []
	for _ in range(4):
		algorithm.Four_Numbers.append(random.randint(1, 13))
	printer('\n')
	printer('OK!')
	time.sleep(0.2)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	printer("Here is four numbers: %d , %d , %d , %d ." % (
		algorithm.Four_Numbers[0], algorithm.Four_Numbers[1], algorithm.Four_Numbers[2], algorithm.Four_Numbers[3]))
	time.sleep(1)
	
	algorithm.calculate_the_whole_answers()
	
	printer("Do you think there are any answers?")
	
	button_yes.configure(command=lambda: whether_have_answers(True))
	button_no.configure(command=lambda: whether_have_answers(False))
	button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
	button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
	
	state_of_change_mode.set('normal')


def clicked_no():
	state_of_change_mode.set('disable')
	
	button_yes.place_forget()
	button_no.place_forget()
	
	printer('\n')
	printer("OK!")
	printer("See you next time!")
	
	button_close.place(relx=0, rely=0, relwidth=1, relheight=1)
	
	state_of_change_mode.set('normal')


def solve_each_question(questions, index, input):
	state_of_change_mode.set('disable')
	
	if input is True:
		algorithm.Four_Numbers = []
		algorithm.Whole_Answers = []
		question = questions[index].split(', ')
		if len(question) == 4:
			format_correct = True
			for step in range(len(question)):
				try:
					question[step] = int(question[step])
				except ValueError:
					format_correct = False
					break
		else:
			format_correct = False
		if format_correct is True:
			for integer in question:
				algorithm.Four_Numbers.append(integer)
			algorithm.calculate_the_whole_answers()
			if len(algorithm.Whole_Answers) == 0:
				printer("There is no any answers!")
			else:
				for Each_Answer in algorithm.Whole_Answers:
					printer(Each_Answer + "=24")
		else:
			printer("Your question's format can not be calculated!")
	
	if index == len(questions) - 1 or input is False:
		button_again.place(relx=0, rely=0.9, relwidth=0.5, relheight=0.1)
		button_close.place(relx=0.5, rely=0.9, relwidth=0.5, relheight=0.1)
		state_of_change_mode.set('normal')
	else:
		button_next.configure(
			command=lambda list_questions=questions, new_index=index + 1: solve_each_question(list_questions, new_index,
			                                                                                  True))
		button_next.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
		state_of_change_mode.set('normal')


def submit_questions():
	state_of_change_mode.set('disable')
	
	submit.configure(state=DISABLED)
	submit.place_forget()
	input_text.configure(state=DISABLED)
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	questions = input_text.get('1.0', 'end')
	questions = questions.split('\n')
	questions.pop()
	if questions == ['']:
		printer("You did not input any questions!")
		solve_each_question(questions, 0, False)
	else:
		solve_each_question(questions, 0, True)


def start(game_mode):
	global mode
	
	if len(root.winfo_children()) != 0:
		windows = root.winfo_children()
		for window in windows:
			if type(window) is tkinter.Toplevel:
				window.destroy()
	
	state_of_change_mode.set('disable')
	
	button_game_mode.pack_forget()
	button_answer_mode.pack_forget()
	
	print_frame_border.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.9)
	print_text.configure(state=DISABLED)
	print_text.place(relx=0, rely=0, relwidth=1, relheight=1)
	input_frame_border.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.9)
	input_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
	
	print_text.configure(state=NORMAL)
	print_text.delete('1.0', 'end')
	print_text.configure(state=DISABLED)
	input_text.configure(state=NORMAL)
	input_text.delete('1.0', 'end')
	input_text.configure(state=DISABLED)
	example.configure(state=NORMAL)
	example.delete('1.0', 'end')
	example.configure(state=DISABLED)
	
	if game_mode:
		mode = 1
		setting.configure(command=lambda: open_setting_window())
		setting.place(relx=0, rely=0, relwidth=1, relheight=0.1)
		printer("Hello! Here is game mode!")
		printer("Here is a game:")
		printer("There will have four random integers from 1 to 13, you need to use these four integers calculate 24.")
		printer("Each integer must and can only be used once.")
		printer("You only could use '+', '-', '*' and '/'.")
		printer("Sometimes, there is no solutions for figuring out 24.")
		printer("\n")
		
		printer("Do you want to play it with me?")
		button_yes.configure(command=lambda: clicked_yes())
		button_no.configure(command=lambda: clicked_no())
		button_yes.place(relx=0, rely=0, relwidth=1, relheight=0.5)
		button_no.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)
		
		state_of_change_mode.set('normal')
	else:
		mode = 2
		setting.configure(command=lambda: open_setting_window())
		setting.place(relx=0, rely=0, relwidth=1, relheight=0.1)
		printer("Hello! Here is answer mode!")
		printer("You can input four integers from 1 to 13.")
		printer("I will print all the answers that can use them to calculate 24.")
		printer("Four integers are a group.")
		printer("Each line writes one group.")
		
		example.configure(state=NORMAL)
		example.delete('1.0', 'end')
		example.configure(state=DISABLED)
		example.place(relx=0, rely=0, relwidth=1, relheight=0.1)
		input_text.configure(state=NORMAL)
		input_text.delete('1.0', 'end')
		input_text.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
		#
		submit.configure(command=lambda: submit_questions())
		submit.configure(state=NORMAL)
		submit.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
		printer("Example: a, b, c, d", example)
		
		state_of_change_mode.set('normal')


button_game_mode.configure(command=lambda: start(True))
button_answer_mode.configure(command=lambda: start(False))

button_again.configure(command=lambda: start(False))


def selected_mode():
	global mode
	mode = 3
	if len(root.winfo_children()) != 0:
		windows = root.winfo_children()
		for window in windows:
			if type(window) is tkinter.Toplevel:
				window.destroy()
	Start.place_forget()
	for content_name in setting_content:
		if type(content_name) is str:
			continue
		content_name.place_forget()
		content_name.pack_forget()
	print_frame_border.place_forget()
	input_frame_border.place_forget()
	input_frame.place_forget()
	open_setting_window()
	button_game_mode.pack(side='top', expand=True)
	button_answer_mode.pack(side='bottom', expand=True)
	root.update_idletasks()


Start.configure(command=lambda: selected_mode())
Start.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()