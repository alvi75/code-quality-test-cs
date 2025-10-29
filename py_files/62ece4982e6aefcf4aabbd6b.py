def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	return [cls] + list(set([c for c in cls.__subclasses__()] + [c for c in subclasses(c) for c in cls.__subclasses__()]))