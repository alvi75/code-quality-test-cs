def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	ordering = []
	for ordering_ in orderings:
		if not ordering_:
			continue
		for element in ordering_:
			if element not in ordering:
				ordering.append(element)
	return ordering