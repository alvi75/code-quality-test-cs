def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	if not keys:
		keys = self.index
	return [self.data[key] for key in keys]