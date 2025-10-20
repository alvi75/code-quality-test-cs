def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	return [c for c in classes if not any(c.isSubclassOf(d) for d in classes)]