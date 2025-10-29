def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self._size:
		raise KeyError('popitem(): dictionary is empty')
	key, value = self._heap[0]
	self._size -= 1
	del self._dict[key]
	return key, value