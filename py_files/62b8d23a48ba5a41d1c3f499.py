def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._size == 0:
		raise KeyError('popitem(): dictionary is empty')
	key = next(iter(self))
	del self[key]
	return (key, self[key])