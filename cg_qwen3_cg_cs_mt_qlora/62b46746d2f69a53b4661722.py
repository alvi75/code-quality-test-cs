def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 0:
		return []
	elif len(args) == 1:
		return self._absorb(args[0])
	else:
		return [self._absorb(arg) for arg in args]