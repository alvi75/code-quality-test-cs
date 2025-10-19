def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if not isinstance(args, (list, tuple)):
		return [self.absorb([args])]
	elif len(args) == 0:
		return []
	elif len(args) == 1:
		return self.absorb(args[0])
	else:
		first = self.absorb(args[0])
		return self.absorb(first + self.absorb(args[1:]))