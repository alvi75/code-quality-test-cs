def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	orderings = [set(x) for x in orderings]
	return sorted(list(set(itertools.chain(*orderings))))