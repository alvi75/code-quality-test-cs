def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self._isClassAttribute():
		raise AttributeError("This is not a class attribute.")
	return (self.name(), self.description(all))