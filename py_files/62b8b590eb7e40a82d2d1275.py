def _legacy_mergeOrderings(orderings):
	"""
	Combine multiple lists in the sequence of occurrence into a list with no duplicate elements.
	"""
	ordering = []
	for orderingComponents in orderings:
		for orderingComponent in orderingComponents:
			if orderingComponent not in ordering:
				ordering.append(orderingComponent)
	return ordering