def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if not self._cache:
		raise KeyError('popitem(): cache is empty')
	key = next(iter(self._cache))
	return key, self._cache.pop(key)