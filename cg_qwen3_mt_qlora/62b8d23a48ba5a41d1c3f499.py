def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._lru is None:
		raise KeyError('popitem() from empty LRU')
	key, value = self._lru.popitem(last=False)
	self._dict.pop(key)
	return key, value