def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if all:
		return [(name, self.describe(name)) for name in self.names()]
	else:
		return [(name, self.describe(name)) for name in self.names() if self.isVisible(name)]