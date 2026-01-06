def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	key = self._popitem()
	if key is not None:
		return (self[key], self.pop(key))