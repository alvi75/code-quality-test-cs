def data(self, *keys):
	"""
	Returns the keys processed by the transform method of the RecordExporter class.
	"""
	if not keys:
		keys = self.keys
	return [self.transform(key, self.record[key]) for key in keys]