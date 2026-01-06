def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if not self._isClassAttribute():
		raise AttributeError("This is not a class attribute.")
	names = []
	descriptions = []
	for attr in self._classAttributes:
		name = attr.name
		desc = attr.description
		if desc == None or (all and desc != ""):
			names.append(name)
			descriptions.append(desc)
	return names, descriptions