def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if all:
		return [(name, self.getDescription(name)) for name in self.names()]
	else:
		return (self.name, self.description)