answer = ['(', 10.0, '+', 7.0, '-', 5.0, ')', '*', 2.0]
Operators = ['+', '-', '*', '/']


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
		elif type(symbol) is float:
			if step > 0 :
				if answer[step - 1] not in Operators and answer[step - 1] != '(':
					return False
			if step < len(answer) - 1:
				if answer[step + 1] not in Operators and answer[step + 1] != ')':
					return False
		elif type(symbol) is str:
			if symbol == '(':
				if len(answer) - step <= 4:
					return False
				elif type(answer[step + 1]) is not float and answer[step + 1] != '(':
					return False
				elif answer[step - 1] not in Operators and answer[step - 1] != '(':
					return False
			elif symbol == ')':
				if step <= 3:
					return False
				elif type(answer[step - 1]) is not float and answer[step - 1] != ')':
					return False
				elif answer[step + 1] not in Operators and answer[step + 1] != ')':
					return False
			elif symbol in Operators:
				if type(answer[step - 1]) is not float and answer[step - 1] != ')':
					return False
				elif type(answer[step + 1]) is not float and answer[step - 1] != '(':
					return False
			else:
				return False
	if len(opening_bracket) != len(back_bracket):
		return False
	return True


print(check_format(answer))