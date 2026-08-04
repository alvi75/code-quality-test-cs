def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._targetClass is None:
		if self._fallback:
			self._targetClass = self._fallback
		else:
			self._targetClass = self._py
	return self._targetClass