def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if len(keys) == 0:
		return self._data

	if isinstance(keys[0], str):
		keys = [self._key for self._key in keys]

	return dict((k, getattr(self, k)) for k in keys)