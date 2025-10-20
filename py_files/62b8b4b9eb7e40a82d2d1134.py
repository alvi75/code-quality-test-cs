def namesAndDescriptions(self, all=False):
	"""
	Returns the name and description of the current class attribute.
	"""
	if self._name is None:
		return []
	names = [self._name]
	descriptions = [self._description]
	if all:
		for attr in self._attributes.values():
			names.extend(attr.namesAndDescriptions(all))
			descriptions.extend(attr.descriptions)
	return names, descriptions