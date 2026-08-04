def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self._map:
		raise KeyError('dictionary is empty')
	key, value = self._map.popitem()
	del self._counts[key]
	return key, value