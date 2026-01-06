def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if self._transform is None:
		raise ValueError("No transform defined for this record")
	return self._transform.data(*keys)