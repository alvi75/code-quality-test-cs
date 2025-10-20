def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._target is None:
		raise NotImplementedError("No target class defined")
	return self._target[:-4] if self._target.endswith('Py') else self._target