def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._size == 0:
		raise KeyError('popitem from empty LRUQueue')
	key = self._keys[self._tail]
	value = self._values[key]
	self._remove(key)
	return key, value