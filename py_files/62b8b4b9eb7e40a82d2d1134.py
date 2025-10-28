def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if self._name is None:
		self._name = self.__class__.__name__
		if self._description is None:
			self._description = self.__doc__.strip()
		else:
			self._description = self._description.strip()

	return (self._name, self._description)