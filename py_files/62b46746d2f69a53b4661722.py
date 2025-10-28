def absorb(self, args):
	"""
	Given an `args` sequence of expressions, return a new list of expression applying absorption.
	"""
	if len(args) == 0:
		return []
	elif len(args) == 1:
		return [args[0]]
	else:
		result = []
		for i in range(len(args)):
			for j in range(i+1,len(args)):
				result.append(And(args[i],args[j]))
		return result