def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"
	if self._keys:
		key = self._keys.pop()
		return key, self[key]
	else:
		raise KeyError('popitem() on empty dictionary')