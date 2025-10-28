def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	key, value = self._popitem()
	self._update_stats()
	return key, value