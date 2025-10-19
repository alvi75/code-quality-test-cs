def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	return [self._absorb(a) for a in args]