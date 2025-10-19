def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self._order is None:
		return dict.popitem(self)
	index = min(enumerate(self._order), key=itemgetter(1))[0]
	key = self._keys[index]
	del self._keys[index]
	return key, self[key]