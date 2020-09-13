def calc(exp: str):
	if '+' in exp:
		exp = [calc(sub_exp) for sub_exp in exp.split('+')]
		result = 0
		for num in exp:
			result += num
		return result
	if '-' in exp:
		exp = [calc(sub_exp) for sub_exp in exp.split('-')]
		result = exp[0]
		for num in exp[1:]:
			result -= num
		return result
	if '*' in exp:
		exp = [calc(sub_exp) for sub_exp in exp.split('*')]
		result = 1
		for num in exp:
			result *= num
		return result
	if '/' in exp:
		exp = [calc(sub_exp) for sub_exp in exp.split('/')]
		result = exp[0]
		for num in exp[1:]:
			result /= num
		return result
	if '^' in exp:
		exp = [calc(sub_exp) for sub_exp in exp.split('^', 1)]
		result = exp[0] ** exp[1]
		return result
	return int(exp) if exp.isdigit() else 0
