def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if self._exporter is None:
		raise Exception("No exporter set")
	return self._exporter.data(*keys)