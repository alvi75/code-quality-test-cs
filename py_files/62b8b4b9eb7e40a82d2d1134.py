def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self._namesAndDescriptions:
		self._namesAndDescriptions = {}
		for attr in dir(self):
			if not attr.startswith('_') or all:
				self._namesAndDescriptions[attr] = getattr(self, attr).__doc__
	return self._namesAndDescriptions