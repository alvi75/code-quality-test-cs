def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	key, value = self._popitem()
	self._size -= 1
	return key, value