def namesAndDescriptions(self, all=False):
		"""
		Returns the name and description of the current class attribute.
		"""
		names = []
		descriptions = []
		for attr in self.__dict__:
			if not attr.startswith('_'):
				names.append(attr)
				descriptions.append(self.__dict__[attr].__doc__)
		return names, descriptions