def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self:
		raise KeyError('popitem(): empty dictionary')
	return self._map.popitem()