def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	if len(keys) == 1:
		return [self.index[k] for k in keys[0]]
	else:
		return [self.index[k] for k in keys]