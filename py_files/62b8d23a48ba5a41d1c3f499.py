def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._cache is None:
		raise KeyError('popitem(): empty cache')
	key = self._cache.pop()
	value = self._cache[key]
	del self._cache[key]
	return key, value