def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	ordering = []
	for o in orderings:
		if not isinstance(o, (list, tuple)):
			o = [o]
		for e in o:
			if e not in ordering:
				ordering.append(e)
	return ordering