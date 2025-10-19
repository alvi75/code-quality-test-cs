def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	classes = set(classes)
	for cls in classes:
		subclasses = set(cls.__subclasses__())
		classes -= subclasses
	return list(classes)