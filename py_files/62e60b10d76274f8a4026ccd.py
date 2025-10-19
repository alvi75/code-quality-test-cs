def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if len(keys) == 1:
		return self._data[keys[0]]
	else:
		result = {}
		for key in keys:
			result[key] = self._data[key]
		return result