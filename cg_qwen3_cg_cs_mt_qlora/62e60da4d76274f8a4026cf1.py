def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	return [self[index] for index in keys]