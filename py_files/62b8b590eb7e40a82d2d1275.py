def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	if not isinstance(orderings, list):
		orderings = [orderings]
	for ordering in orderings:
		if not isinstance(ordering, list):
			raise ValueError("Each ordering must be a list.")
	return sorted(set(itertools.chain.from_iterable(ordering)))