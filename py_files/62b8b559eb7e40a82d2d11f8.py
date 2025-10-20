def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	return [c for c in classes if not any(c in b.__bases__ for b in classes)]