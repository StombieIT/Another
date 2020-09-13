def calc(exp: str):
	if '-' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('-'))
		res = next(exp)
		for num in exp:
			res -= num
		del num
		return res
	if '+' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('+'))
		res = 0
		for num in exp:
			res += num
		del num
		return res
	if '%' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('%'))
		res = next(exp)
		for num in exp:
			res %= num
		del num
		return res
	if '//' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('//'))
		res = next(exp)
		for num in exp:
			res //= num
		del num
		return res
	if '/' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('/'))
		res = next(exp)
		for num in exp:
			res /= num
		del num
		return res
	if '*' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('*'))
		res = 1
		for num in exp:
			res *= num
		del num
		return res
	if '^' in exp:
		exp = (calc(sub_exp) for sub_exp in exp.split('^', 1))
		res = next(exp) ** next(exp)
		return res
	return int(exp) if exp.isdigit() else 0
