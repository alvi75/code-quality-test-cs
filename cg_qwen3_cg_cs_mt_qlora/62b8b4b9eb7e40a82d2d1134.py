def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if self._namesAndDescriptions is None:
		self._namesAndDescriptions = {}
		for attr in dir(self):
			if not attr.startswith('_') and not callable(getattr(self, attr)):
				self._namesAndDescriptions[attr] = getattr(self, attr).__doc__
	return self._namesAndDescriptions