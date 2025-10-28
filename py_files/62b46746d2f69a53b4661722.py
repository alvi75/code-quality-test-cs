def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 1:
		return args[0]
	elif len(args) == 2:
		return [self.absorb(args[0], args[1])]
	else:
		return [self.absorb(a) for a in args]