def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	merged = []
	for ordering in sorted(orderings, key=lambda x: len(x)):
		if not merged or ordering[0] != merged[-1][1]:
			merged.append(ordering)
	return merged