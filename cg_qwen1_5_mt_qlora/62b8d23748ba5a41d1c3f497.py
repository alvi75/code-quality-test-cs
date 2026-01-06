def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._size == 0:
		raise KeyError('popitem(): dictionary is empty')
	key = self._min()
	del self[key]
	return (key, self[key])