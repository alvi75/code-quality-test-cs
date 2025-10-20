def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self._size == 0:
		raise KeyError("popitem(): dictionary is empty")
	key = self._keys[-1]
	value = self._values.pop()
	self._keys.pop()
	self._size -= 1
	return key, value