def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not self.__class__.__name__ in self._names:
		self._names[self.__class__.__name__] = []
		for attr in dir(self.__class__):
			if attr[0] != '_' and not attr.startswith('__'):
				self._names[self.__class__.__name__].append(attr)
	return self._names[self.__class__.__name__]