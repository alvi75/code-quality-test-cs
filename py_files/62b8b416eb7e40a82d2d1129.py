def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	names = []
	for name in dir(self.__class__):
		if not all and name.startswith('_'): continue
		names.append(name)
	return names