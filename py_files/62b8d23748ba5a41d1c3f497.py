def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self:
		raise KeyError('popitem(): dictionary is empty')
	freq = min(self._freq.values())
	return self._popitem(freq)