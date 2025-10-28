def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	return [c for c in cls.__subclasses__()] + \
			[cls.subclasses() for c in cls.__subclasses__()]

	# return [c for c in cls.__subclasses__() if not c.__name__.startswith('_')]
	# return [c for c in cls.__subclasses__() if not c.__name__.startswith('_') and not c.__name__.startswith('Meta')]