def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	if not isinstance(orderings, (list, tuple)):
		raise TypeError("orderings must be a list or tuple")
	return sorted(set(itertools.chain.from_iterable(orderings)))