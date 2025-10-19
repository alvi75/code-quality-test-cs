def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	names = self.names(all)
	descriptions = self.descriptions(all)
	return zip(names, descriptions)