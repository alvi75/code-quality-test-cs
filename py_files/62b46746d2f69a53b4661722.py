def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	result = []
	for arg in args:
		if result and result[-1].is_identity():
			if arg.is_identity():
				continue
			elif arg.is_negation():
				arg = arg.arg
			if arg in result[-1]:
				continue
		result.append(arg)
	return result