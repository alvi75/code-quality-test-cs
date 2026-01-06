def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self._name:
		self._name = self.__class__.__name__
	if not self._description:
		self._description = self.__doc__ if self.__doc__ else None
	return self._name, self._description