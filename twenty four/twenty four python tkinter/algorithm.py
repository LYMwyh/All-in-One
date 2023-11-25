Operators = ['+', '-', '*', '/']
answer = []
complete_answer = []

Whole_Answers = []
the_Selected_Operators = []
Four_Numbers = []

one_group = 0
abc = 0


class Fraction(object):
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator


def check_format(answer):
	global Operators
	opening_bracket = []
	back_bracket = []
	for step in range(len(answer)):
		symbol = answer[step]
		if symbol == '(':
			opening_bracket.append(step)
			if len(opening_bracket) > 1:
				if opening_bracket[-1] - opening_bracket[-2] == 1:
					return False
		elif symbol == ')':
			back_bracket.append(step)
			if len(opening_bracket) < len(back_bracket):
				return False
			elif back_bracket[-1] - opening_bracket[-1] <= 1:
				return False
			if len(back_bracket) > 1:
				if back_bracket[-1] - back_bracket[-2] == 1:
					return False
		elif type(symbol) is int:
			if step > 0:
				if answer[step - 1] not in Operators and answer[step - 1] != '(':
					return False
			if step < len(answer) - 1:
				if answer[step + 1] not in Operators and answer[step + 1] != ')':
					return False
		elif type(symbol) is str:
			if symbol == '(':
				if len(answer) - step <= 4:
					return False
				elif type(answer[step + 1]) is not int and answer[step + 1] != '(':
					return False
				elif answer[step - 1] not in Operators and answer[step - 1] != '(':
					return False
			elif symbol == ')':
				if step <= 3:
					return False
				elif type(answer[step - 1]) is not int and answer[step - 1] != ')':
					return False
				elif answer[step + 1] not in Operators and answer[step + 1] != ')':
					return False
			elif symbol in Operators:
				if type(answer[step - 1]) is not int and answer[step - 1] != ')':
					return False
				elif type(answer[step + 1]) is not int and answer[step - 1] != '(':
					return False
			else:
				return False
	if len(opening_bracket) != len(back_bracket):
		return False
	return True


def before_or_after_one(index_of_one, before, complete_answer):
	if before is True:
		if complete_answer[index_of_one + 1] == "/":
			return "", -1
		elif complete_answer[index_of_one + 1] == "+":
			return "", len(complete_answer)
		elif complete_answer[index_of_one + 1] == "-":
			return "-", len(complete_answer)
		before = -1
	else:
		if complete_answer[index_of_one - 1] == "+" or complete_answer[index_of_one - 1] == "-":
			return "", len(complete_answer)
		before = 1
	while True:
		index_of_one += before
		if index_of_one < 0 or index_of_one >= len(complete_answer):
			return "", len(complete_answer)
		if complete_answer[index_of_one] == "(" or complete_answer[index_of_one] == ")":
			return complete_answer[index_of_one], len(complete_answer)
		if complete_answer[index_of_one] == "+":
			return "+", len(complete_answer)
		if before == -1:
			if complete_answer[index_of_one] == "/":
				return "/", index_of_one
			if complete_answer[index_of_one] == "-":
				return "-", index_of_one
		elif before == 1 and complete_answer[index_of_one] == "-":
			return "-", len(complete_answer)
		if complete_answer[index_of_one] != 1:
			return complete_answer[index_of_one], index_of_one


def simplify_formula_first_part(complete_answer):
	layer = 0
	whether_found_addition_or_subtraction = [False]
	whether_found_multiplication_or_division = [False]
	brackets = []
	step = 0
	whether_changed = False
	while True:
		if step == len(complete_answer):
			if whether_changed is False:
				break
			else:
				step = 0
				whether_changed = False
		# brackets.clear()
		symbol = complete_answer[step]
		if symbol == '(':
			layer += 1
			if len(whether_found_multiplication_or_division) == layer:
				whether_found_multiplication_or_division.append(False)
				whether_found_addition_or_subtraction.append(False)
			else:
				whether_found_multiplication_or_division[layer] = False
				whether_found_addition_or_subtraction[layer] = False
			brackets.append(step)
		if symbol == ')':
			decision_front = False
			decision_back = False
			change_symbol_from_subtraction = False
			change_symbol_from_division = False
			if whether_found_multiplication_or_division[layer] and whether_found_addition_or_subtraction[
				layer] is False:
				decision_front = True
				decision_back = True
				if brackets[layer - 1] != 0 and complete_answer[brackets[layer - 1] - 1] == '/':
					change_symbol_from_division = True
			elif brackets[layer - 1] != 0 and complete_answer[brackets[layer - 1] - 1] == '/':
				pass
			else:
				if brackets[layer - 1] != 0:
					if complete_answer[brackets[layer - 1] - 1] != '*' and complete_answer[
						brackets[layer - 1] - 1] != '/':
						decision_front = True
						if complete_answer[brackets[layer - 1] - 1] == '-':
							change_symbol_from_subtraction = True
					elif complete_answer[brackets[layer - 1] - 2] == 1:
						temporary_symbol, temporary_index = before_or_after_one(brackets[layer - 1] - 2, True, complete_answer)
						if temporary_symbol == "/":
							pass
						elif type(temporary_symbol) is int:
							pass
						else:
							decision_front = True
						if temporary_symbol == "-":
							change_symbol_from_subtraction = True
				else:
					decision_front = True
				if step != len(complete_answer) - 1:
					if complete_answer[step + 1] != '*' and complete_answer[step + 1] != '/':
						decision_back = True
					elif complete_answer[step + 2] == 1:
						temporary_symbol, temporary_index = before_or_after_one(step + 2, False, complete_answer)
						if type(temporary_symbol) is int:
							pass
						else:
							decision_back = True
				else:
					decision_back = True
			if decision_front and decision_back:
				whether_changed = True
				if change_symbol_from_subtraction or change_symbol_from_division:
					temporary_layer = 0
					for temporary_step in range(brackets[layer - 1] + 1, step):
						if change_symbol_from_subtraction and temporary_layer == 0 and complete_answer[
							temporary_step] == '+':
							complete_answer[temporary_step] = '-'
						elif change_symbol_from_subtraction and temporary_layer == 0 and complete_answer[
							temporary_step] == '-':
							complete_answer[temporary_step] = '+'
						elif change_symbol_from_division and temporary_layer == 0 and complete_answer[
							temporary_step] == '*':
							complete_answer[temporary_step] = '/'
						elif change_symbol_from_division and temporary_layer == 0 and complete_answer[
							temporary_step] == '/':
							complete_answer[temporary_step] = '*'
						elif complete_answer[temporary_step] == '(':
							temporary_layer += 1
						elif complete_answer[temporary_step] == ')':
							temporary_layer -= 1
				if whether_found_multiplication_or_division[layer]:
					whether_found_multiplication_or_division[layer - 1] = True
				if whether_found_addition_or_subtraction[layer]:
					whether_found_addition_or_subtraction[layer - 1] = True
				complete_answer.pop(brackets[layer - 1])
				complete_answer.pop(step - 1)
				step -= 2
			brackets.pop()
			layer -= 1
		if symbol == '+' or symbol == '-':
			whether_found_addition_or_subtraction[layer] = True
		elif symbol == '*' or symbol == '/':
			whether_found_multiplication_or_division[layer] = True
		step += 1
	return complete_answer


def simplify_formula_third_part(part_of_group):
	# ['+', 121.0, '/', 11.0, '*', 4.0]
	if len(part_of_group) < 3:
		return part_of_group
	# [39.0, '-', 26.0]
	sort_list = []
	for step in range(len(part_of_group)):
		symbol = part_of_group[step]
		if type(symbol) is not str:
			sort_list.append(
				{"representative": str(part_of_group[step]) if type(part_of_group[step]) is not list else ''.join(list(map(str, part_of_group[step]))), "operator": part_of_group[step - 1], "index": step})
	min_number = 0
	for step in range(len(sort_list)):
		element = sort_list[step]
		if element["operator"] == '*' and sort_list[min_number]["representative"] > element["representative"]:
			min_number = step
	if min_number != 0:
		part_of_group[sort_list[0]["index"]], part_of_group[sort_list[min_number]["index"]] = part_of_group[
			sort_list[min_number]["index"]], part_of_group[sort_list[0]["index"]]
		sort_list[min_number]["representative"] = sort_list[0]["representative"]
	first_number = sort_list[0]["index"] + 1
	del sort_list[0]
	sort_list.sort(reverse=False, key=lambda sort_num: sort_num["representative"])
	new_list = [_ for _ in part_of_group[0:first_number]]
	index_of_sort_list = 0
	for step in range(first_number, len(part_of_group), 2):
		index = sort_list[index_of_sort_list]["index"]
		new_list.append(part_of_group[index - 1])
		new_list.append(part_of_group[index])
		index_of_sort_list += 1
	return new_list


def split_list(whole_list):
	if type(whole_list) is list:
		new_list = []
		for part_of_list in whole_list:
			temporary_list = split_list(part_of_list)
			if type(temporary_list) is not list:
				new_list.append(temporary_list)
			else:
				for symbol in temporary_list:
					new_list.append(symbol)
		return new_list
	else:
		return whole_list


def simplify_formula_forth_part(group):
	compare_nums = []
	for step in range(len(group)):
		part_of_group = group[step]
		compare_nums.append({"representative": ''.join(list(map(str, part_of_group))), "operator": part_of_group[0], "index": step})
	compare_nums.sort(reverse=False, key=lambda sort_num: sort_num["representative"])
	for step in range(len(compare_nums)):
		element = compare_nums[step]
		if element["operator"] == '+':
			compare_nums[0], compare_nums[step] = compare_nums[step], compare_nums[0]
			break
	new_group = []
	for element in compare_nums:
		temporary_group = split_list(group[element["index"]])
		for symbol in temporary_group:
			new_group.append(symbol)
	del new_group[0]
	return new_group


def simplify_formula_second_part(first, complete_answer, layer):
	global one_group, abc
	group = []
	temporary_group = ['+']
	step = first
	while step < len(complete_answer):
		symbol = complete_answer[step]
		if symbol == '+' or symbol == '-':
			temporary_step = 0
			while temporary_step < len(temporary_group):
				temporary_symbol = temporary_group[temporary_step]
				if temporary_symbol == 1:
					if len(temporary_group) == 2:
						break
					elif temporary_step == 1 and temporary_group[temporary_step + 1] == '/':
						temporary_step += 1
						continue
					elif temporary_step == 1 and temporary_group[temporary_step + 1] == '*':
						del temporary_group[temporary_step]
						del temporary_group[temporary_step]
					else:
						del temporary_group[temporary_step - 1]
						del temporary_group[temporary_step - 1]
					temporary_step -= 2
					one_group += 1
				temporary_step += 1
			temporary_group = simplify_formula_third_part(temporary_group)
			# print(temporary_group, 1)
			group.append([_ for _ in temporary_group[:]])
			temporary_group.clear()
		
		if symbol == '(':
			temporary_list, step = simplify_formula_second_part(step + 1, complete_answer, layer + 1)
			temporary_list.insert(0, '(')
			temporary_list.append(')')
			temporary_group.append([_ for _ in temporary_list])
			step += 1
			continue
		if symbol == ')':
			break
		temporary_group.append(symbol)
		step += 1
	
	temporary_step = 0
	while temporary_step < len(temporary_group):
		temporary_symbol = temporary_group[temporary_step]
		if temporary_symbol == 1:
			if len(temporary_group) == 2:
				break
			elif temporary_step == 1 and temporary_group[temporary_step + 1] == '/':
				temporary_step += 1
				continue
			elif temporary_step == 1 and temporary_group[temporary_step + 1] == '*':
				del temporary_group[temporary_step]
				del temporary_group[temporary_step]
			else:
				del temporary_group[temporary_step - 1]
				del temporary_group[temporary_step - 1]
			temporary_step -= 2
			one_group += 1
		temporary_step += 1
	
	temporary_group = simplify_formula_third_part(temporary_group)
	
	group.append([_ for _ in temporary_group[:]])
	temporary_group.clear()
	if layer == 0:
		while one_group:
			one_group -= 1
			group.append(['*', 1])
	
	# print(temporary_group, 2)
	group = simplify_formula_forth_part(group)
	# print(group, 3)
	return group, step


def calculate_the_answer():
	global answer
	step = 0
	layer = 0
	whether_use_addition_and_subtraction = [False]
	whether_use_multiplication_and_division = [True]
	whether_found_multiplication_or_division = [False]
	while len(answer) != 1:
		# print(answer)
		if step == len(answer):
			step = 0
			whether_use_addition_and_subtraction = [not i for i in whether_found_multiplication_or_division]
			whether_use_multiplication_and_division = [True for _ in whether_use_multiplication_and_division]
			whether_found_multiplication_or_division = [False for _ in whether_found_multiplication_or_division]
		symbol = answer[step]
		if symbol == '(':
			if len(whether_found_multiplication_or_division) - 1 == layer:
				whether_found_multiplication_or_division.append(False)
				whether_use_multiplication_and_division.append(True)
				whether_use_addition_and_subtraction.append(False)
			layer += 1
			step += 1
			continue
		if symbol == ')':
			layer -= 1
			if answer[step - 2] == '(':
				answer.pop(step - 2)
				answer.pop(step - 1)
				step -= 1
			else:
				step += 1
			continue
		if whether_use_addition_and_subtraction[layer]:
			if symbol == '+':
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[
					step + 1] == ')':
					pass
				else:
					if answer[step - 2] != '-':
						answer[step - 1].numerator *= answer[step + 1].denominator
						answer[step + 1].numerator *= answer[step - 1].denominator
						answer[step - 1].numerator += answer[step + 1].numerator
						answer[step - 1].denominator *= answer[step + 1].denominator
					else:
						answer[step - 1].numerator *= answer[step + 1].denominator
						answer[step + 1].numerator *= answer[step - 1].denominator
						answer[step - 1].numerator -= answer[step + 1].numerator
						answer[step - 1].denominator *= answer[step + 1].denominator
					del answer[step: step + 2]
					continue
			elif symbol == '-':
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[
					step + 1] == ')':
					pass
				else:
					if answer[step - 2] != '-':
						answer[step - 1].numerator *= answer[step + 1].denominator
						answer[step + 1].numerator *= answer[step - 1].denominator
						answer[step - 1].numerator -= answer[step + 1].numerator
						answer[step - 1].denominator *= answer[step + 1].denominator
					else:
						answer[step - 1].numerator *= answer[step + 1].denominator
						answer[step + 1].numerator *= answer[step - 1].denominator
						answer[step - 1].numerator += answer[step + 1].numerator
						answer[step - 1].denominator *= answer[step + 1].denominator
					del answer[step: step + 2]
					continue
		if whether_use_multiplication_and_division[layer]:
			if symbol == '*':
				whether_found_multiplication_or_division[layer] = True
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[
					step + 1] == ')':
					whether_use_multiplication_and_division[layer] = False
				else:
					answer[step - 1].numerator *= answer[step + 1].numerator
					answer[step - 1].denominator *= answer[step + 1].denominator
					del answer[step: step + 2]
					continue
			elif symbol == '/':
				whether_found_multiplication_or_division[layer] = True
				if answer[step - 1] == '(' or answer[step - 1] == ')' or answer[step + 1] == '(' or answer[
					step + 1] == ')':
					whether_use_multiplication_and_division[layer] = False
				else:
					if answer[step + 1] == 0:
						answer = [0]
						break
					answer[step - 1].numerator *= answer[step + 1].denominator
					answer[step - 1].denominator *= answer[step + 1].numerator
					del answer[step: step + 2]
					continue
		step += 1
	if answer[0].denominator == 0:
		answer[0] = 0
	elif answer[0].numerator % answer[0].denominator == 0 and answer[0].numerator / answer[0].denominator == 24:
		answer[0] = 24
	else:
		answer[0] = 0


def calculate_the_whole_answers():
	global answer, Four_Numbers, Operators, the_Selected_Operators, complete_answer, one_group
	for first_element in range(0, 4):
		Four_Numbers[0], Four_Numbers[first_element] = Four_Numbers[first_element], Four_Numbers[0]
		for second_element in range(1, 4):
			Four_Numbers[1], Four_Numbers[second_element] = Four_Numbers[second_element], Four_Numbers[1]
			for third_element in range(2, 4):
				Four_Numbers[2], Four_Numbers[third_element] = Four_Numbers[third_element], Four_Numbers[2]
				
				for the_First_Operator in Operators:
					the_Selected_Operators.append(the_First_Operator)
					for the_Second_Operator in Operators:
						the_Selected_Operators.append(the_Second_Operator)
						for the_third_Operator in Operators:
							the_Selected_Operators.append(the_third_Operator)
							for Type_of_Brackets in range(7):
								# a = Four_Numbers[0]
								# b = Four_Numbers[1]
								# c = Four_Numbers[2]
								# d = Four_Numbers[3]
								answer.clear()
								for Create_the_Answer in range(4):
									# 0. (a b) c d
									# 1. a (b c) d
									# 2. a b (c d)
									# 3. (a b c) d
									# 4. a (b c d)
									# 5. (a b)(c d)
									# 6. a b c d
									if Create_the_Answer == 0 and (
											Type_of_Brackets == 0 or Type_of_Brackets == 3 or Type_of_Brackets == 5):
										answer.append("(")
									elif Create_the_Answer == 1 and (
											Type_of_Brackets == 1 or Type_of_Brackets == 4):
										answer.append("(")
									elif Create_the_Answer == 2 and (
											Type_of_Brackets == 2 or Type_of_Brackets == 5):
										answer.append("(")
									
									answer.append(Fraction(Four_Numbers[Create_the_Answer], 1))
									
									if Create_the_Answer == 1 and (Type_of_Brackets == 0 or Type_of_Brackets == 5):
										answer.append(")")
									elif Create_the_Answer == 2 and (
											Type_of_Brackets == 1 or Type_of_Brackets == 3):
										answer.append(")")
									elif Create_the_Answer == 3 and (
											Type_of_Brackets == 2 or Type_of_Brackets == 4 or Type_of_Brackets == 5):
										answer.append(")")
									
									if Create_the_Answer < 3:  # 0 , 1 , 2
										answer.append(the_Selected_Operators[Create_the_Answer])
								complete_answer = [_ if type(_) is not Fraction else _.numerator for _ in answer]
								calculate_the_answer()
								if answer == [24]:
									old_version_answer = []
									while True:
										one_group = 0
										complete_answer = simplify_formula_first_part(complete_answer)
										complete_answer, temporary_number = simplify_formula_second_part(0,
										                                                                 complete_answer,
										                                                                 0)
										if old_version_answer == complete_answer:
											break
										old_version_answer = [_ for _ in complete_answer]
									# for step in range(len(complete_answer)):
									# 	if type(complete_answer[step]) is float:
									# 		complete_answer[step] = int(complete_answer[step])
									#
									answer = [_ if type(_) is not int else Fraction(_, 1) for _ in complete_answer]
									calculate_the_answer()
									if answer != [24]:
										print("error!")
										print(complete_answer)
									#
									complete_answer = ''.join(list(map(str, complete_answer)))
									if complete_answer not in Whole_Answers:
										Whole_Answers.append(complete_answer)
							
							the_Selected_Operators.pop()
						the_Selected_Operators.pop()
					the_Selected_Operators.pop()
				
				Four_Numbers[2], Four_Numbers[third_element] = Four_Numbers[third_element], Four_Numbers[2]
			Four_Numbers[1], Four_Numbers[second_element] = Four_Numbers[second_element], Four_Numbers[1]
		Four_Numbers[0], Four_Numbers[first_element] = Four_Numbers[first_element], Four_Numbers[0]
