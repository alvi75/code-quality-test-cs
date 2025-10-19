def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	names = self.__dict__.keys()
	if not all:
		names = [name for name in names if not name.startswith('_')]
	return names