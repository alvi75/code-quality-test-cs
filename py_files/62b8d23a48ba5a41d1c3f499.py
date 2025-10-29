def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._cache is None:
		raise KeyError('popitem(): empty cache')
	key, value = self._cache.popitem(last=False)
	self._cache[key] = value
	return key, value