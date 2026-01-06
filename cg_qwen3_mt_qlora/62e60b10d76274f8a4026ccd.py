def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if not self._data:
		self._data = self.transform()
	return self._data.get(*keys)