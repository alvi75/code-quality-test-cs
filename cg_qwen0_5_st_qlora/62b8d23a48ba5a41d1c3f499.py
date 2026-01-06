def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if not self._keys:
		raise KeyError("pop from empty list")
	key = self._keys.pop(0)
	return (key, self._values.pop(key))