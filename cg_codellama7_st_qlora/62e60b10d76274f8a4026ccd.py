def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if not keys:
		return self.data
	return [self.data[key] for key in keys]