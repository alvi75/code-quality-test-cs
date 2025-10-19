def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._size == 0:
		raise KeyError('popitem() called on empty deque')
	key = self._keys[0]
	del self._keys[0], self._values[0]
	return key, self._values[0]