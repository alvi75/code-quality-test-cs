def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	subclasses = cls.__subclasses__()
	for subclass in subclasses:
		subclasses.extend(subclasses(subclass))
	return subclasses