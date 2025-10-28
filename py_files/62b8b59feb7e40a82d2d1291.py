def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._target is None:
		return None
	else:
		return self._target.__class__.__name__[:-6]