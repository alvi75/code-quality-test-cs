def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._size == 0:
		raise KeyError('popitem() called on empty LRU cache')
	key = min(self._cache.keys(), key=self._cache.get)
	value = self[key]
	del self[key]
	return (key, value)