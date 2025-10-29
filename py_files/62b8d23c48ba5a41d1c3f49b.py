def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self._size == 0:
		raise KeyError("pop from empty dictionary")
	key = list(self.keys())[self._size - 1]
	value = self[key]
	del self[key]
	return key, value