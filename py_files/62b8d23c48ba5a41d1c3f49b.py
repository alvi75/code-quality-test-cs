def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"
	"""
	if self._cache is None:
		raise KeyError('popitem(): empty cache')
	return self._cache.popitem()