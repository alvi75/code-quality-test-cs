def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not self._names:
		self._names = [attr for attr in dir(self) if not attr.startswith('_')]
	return self._names if all else self._names[:len(self._names)]