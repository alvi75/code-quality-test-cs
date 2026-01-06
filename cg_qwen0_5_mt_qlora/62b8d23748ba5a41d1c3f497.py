def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if len(self) == 0:
		raise KeyError("pop from empty list")
	self._keys = sorted(self._keys)
	return self._keys.pop(0), self._values.pop(0)