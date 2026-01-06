def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._target_class is None:
		self._target_class = self.__class__.__name__.split('_')[0]
	return self._target_class