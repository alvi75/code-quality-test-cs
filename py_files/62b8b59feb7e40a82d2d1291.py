def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self._targetclass is None:
		self._targetclass = getattr(
			importlib.import_module("py" + self._name),
			self._name.upper() + "PY"
		)
	return self._targetclass