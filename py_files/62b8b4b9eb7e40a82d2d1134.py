def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if self._name is None:
		return []
	names = [self._name]
	if not all:
		return names
	else:
		return names + self._namesAndDescriptions()