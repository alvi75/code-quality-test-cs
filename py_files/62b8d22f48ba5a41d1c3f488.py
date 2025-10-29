def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self._first is None:
		raise KeyError('popitem(): empty')
	key, value = self._first.key, self._first.value
	self._first = self._first.next
	return (key, value)