def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self._first is None:
		raise KeyError('popitem(): dictionary is empty')
	key = self._first.key
	value = self._first.value
	self._remove_node(self._first)
	return (key, value)