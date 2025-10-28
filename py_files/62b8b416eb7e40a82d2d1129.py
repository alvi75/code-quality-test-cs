def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not self._names:
		self._names = [a for a in dir(self) if not a.startswith('_')]
	return self._names