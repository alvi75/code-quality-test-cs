def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	return [cls for cls in classes if not any(cls.isSubclassOf(sub) for sub in classes)]