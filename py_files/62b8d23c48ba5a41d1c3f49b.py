def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self._size == 0:
		raise KeyError('popitem() called on empty deque')
	key = self._keys.popleft()
	value = self._values.popleft()
	self._size -= 1
	return key, value