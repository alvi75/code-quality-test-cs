def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if all:
		return self._all_names
	else:
		return [name for name in self._names if not name.startswith('_')]