def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if cls in cls.__subclasses__:
		return [cls] + cls.subclasses()
	else:
		return []