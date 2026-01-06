def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used."
	"""
	if not self:
		raise KeyError('popitem(): dictionary is empty')
	key, value = self._map.popitem()
	self._setitem(key, value)
	return key, value