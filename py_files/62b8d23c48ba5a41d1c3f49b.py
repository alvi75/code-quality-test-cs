def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self._last is None:
		raise KeyError('popitem(): dictionary is empty')
	key = self._last.key
	self._last = self._last.next
	return key, self._dict.pop(key)