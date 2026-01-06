def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	if keys:
		return [self[key] for key in keys]
	else:
		return [self[key] for key in self.index]