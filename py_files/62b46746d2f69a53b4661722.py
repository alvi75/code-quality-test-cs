def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 0:
		return self

	args = [self._absorb(arg) for arg in args]

	if len(args) == 1:
		return args[0]

	if isinstance(args[0], And):
		return And(*args)

	if isinstance(args[0], Or):
		return Or(*args)

	return And(*args)