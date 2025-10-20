def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if not isinstance(args, (list, tuple)):
		raise TypeError("absorb() argument must be a sequence")
	return [self._apply_absorption(arg) for arg in args]