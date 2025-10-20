def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not hasattr(self, '_namesAndDescriptions'):
		self._namesAndDescriptions = {}
		for attr in self.__class__.__dict__:
			value = getattr(self, attr)
			if isinstance(value, (str, unicode)):
				self._namesAndDescriptions[attr] = value
			elif isinstance(value, (list, tuple)):
				self._namesAndDescriptions[attr] = ', '.join([self.namesAndDescriptions(x) for x in value])
			else:
				self._namesAndDescriptions[attr] = str(value)

	return self._namesAndDescriptions if all else self._namesAndDescriptions[self.name]