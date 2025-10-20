def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	key = self._last_key
	self._remove(key)
	return key, self[key]