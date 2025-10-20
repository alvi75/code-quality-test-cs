def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 0:
		return []
	elif len(args) == 1:
		return [self.absorb_single(args[0])]
	else:
		return self._absorb_multiple(args)