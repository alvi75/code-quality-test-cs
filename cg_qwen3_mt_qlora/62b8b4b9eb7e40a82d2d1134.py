def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	names = []
	descriptions = []
	for attr in self.__class__.attributeNames():
		if not all and attr.startswith('_'):
			continue
		names.append(attr)
		desc = self.__class__.attributeDescription(attr)
		if desc is None:
			desc = ''
		descriptions.append(desc)
	return names, descriptions