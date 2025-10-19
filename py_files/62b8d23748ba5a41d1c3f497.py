def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._size == 0:
		raise KeyError('popitem() called on empty LruDict')
	key = min(self._keys, key=self._freqs.get)
	del self[key]
	return (key, self.pop(key))