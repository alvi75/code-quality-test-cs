def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	for key in keys:
		yield self._transform(key)