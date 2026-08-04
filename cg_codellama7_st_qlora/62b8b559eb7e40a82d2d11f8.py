def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	bases = []
	for c in classes:
		if not c.subclasses:
			bases.append(c)
	return bases