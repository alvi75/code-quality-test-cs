def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self._size == 0:
		raise KeyError('popitem from empty LRUQueue')
	key = self._keys.pop()
	value = self._values.pop(key)
	self._size -= 1
	return key, value