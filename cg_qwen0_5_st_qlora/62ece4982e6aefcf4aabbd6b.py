def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if cls in _subclasses:
		return _subclasses[cls]
	else:
		subclasses = []
		for subclass in cls.__subclasses__():
			subclasses.append(subclass)
		_subclasses[cls] = subclasses
		return subclasses