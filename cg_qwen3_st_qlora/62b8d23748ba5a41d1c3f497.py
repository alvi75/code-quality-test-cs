def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self:
		raise KeyError('popitem(): dictionary is empty')
	key, value = self._map.popitem()
	self._size -= 1
	return key, value