def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 0:
		return []
	elif len(args) == 1:
		expr = args[0]
		if isinstance(expr, Absorption):
			return expr.args + self.absorb([expr.arg])
		else:
			return [expr]
	else:
		first = args[0]
		result = self.absorb(args[1:])
		if isinstance(first, Absorption):
			return result + first.args
		else:
			return [first] + result