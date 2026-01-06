def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if not self._keys:
		raise KeyError("popitem(): dictionary is empty")
	k, v = self._keys.pop(0)
	return k, v