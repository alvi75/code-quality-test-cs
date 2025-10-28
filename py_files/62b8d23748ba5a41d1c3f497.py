def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._size == 0:
		raise KeyError("pop from empty list")
	key, value = self._keys[0], self._values[0]
	self._keys.popleft()
	self._values.popleft()
	return key, value