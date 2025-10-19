def _mergeOrderings(a, b):
		return sorted(set(a + b))
	
	orderings = [list(o) for o in orderings]
	return reduce(_mergeOrderings, orderings)