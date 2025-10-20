def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self.__class__.__name__ in self._namesAndDescriptions:
		self._namesAndDescriptions[self.__class__.__name__] = []
		for attr in dir(self.__class__):
			if attr.startswith('_') or attr == '__init__':
				continue
			if (not all) or (attr in self.__dict__):
				self._namesAndDescriptions[self.__class__.__name__].append((attr, getattr(self, attr)))
	return self._namesAndDescriptions[self.__class__.__name__]