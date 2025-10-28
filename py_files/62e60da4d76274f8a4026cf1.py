def values(self, *keys):
	"""
	Returns the key filtered by self.index in the form of a list.
	"""
	return [self._data[k] for k in keys if k in self._data]