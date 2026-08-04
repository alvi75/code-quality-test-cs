def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	merged = []
	for ordering in orderings:
		for element in ordering:
			if element not in merged:
				merged.append(element)
	return merged