def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._target is None:
		return self.__class__.__name__.split('Py')[0]
	else:
		return self._target