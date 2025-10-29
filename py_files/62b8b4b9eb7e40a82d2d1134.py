def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self.isClass():
		raise AttributeError("Attribute '%s' is not a class attribute." % (self.name))
	return [a.name for a in self.attributes if a.isAttribute() and a.isClass()]