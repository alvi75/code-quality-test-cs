def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	return set([cls] + [c for c in cls.__subclasses__() if not issubclass(c, object)])