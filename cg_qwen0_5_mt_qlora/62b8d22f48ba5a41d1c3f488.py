def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self._size == 0:
		raise KeyError("pop from empty dictionary")
	self._dict.pop(self._keys[0])
	self._keys = self._keys[1:]
	self._size -= 1
	return self._keys[0], self._dict[self._keys[0]]