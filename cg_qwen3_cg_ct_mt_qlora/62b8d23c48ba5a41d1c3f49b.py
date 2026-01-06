def popitem(self):
	"""
	def popitem(self):
	"Remove and return the (key, value) pair most recently used."
	"""
	if self._last is None:
		raise KeyError('popitem(): dictionary is empty')
	key = self._last.key
	value = self._last.value
	self._remove_node(self._last)
	return key, value