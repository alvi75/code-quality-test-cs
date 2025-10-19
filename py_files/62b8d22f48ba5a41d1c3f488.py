def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self._keys:
		key = self._keys[0]
		val = self[key]
		del self[key]
		return (key, val)
	else:
		raise KeyError('popitem() on empty dictionary')