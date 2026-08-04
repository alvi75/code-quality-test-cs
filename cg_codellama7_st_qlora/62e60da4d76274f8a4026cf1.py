def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	if not keys:
		return list(self.index.values())
	return [self.index[key] for key in keys]