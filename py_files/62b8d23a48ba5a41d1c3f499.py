def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._size == 0:
		raise IndexError("pop from empty list")
	self._keys.pop()
	self._values.pop()
	return self._keys[-1], self._values[-1]