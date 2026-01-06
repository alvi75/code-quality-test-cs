def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if not self:
		raise KeyError('popitem(): dictionary is empty')
	return self._dict.popitem()