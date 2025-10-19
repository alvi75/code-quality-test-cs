def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	subclasses = []
	for s in cls.__subclasses__():
		subclasses.append(s)
		subclasses.extend(s.subclasses())
	return subclasses