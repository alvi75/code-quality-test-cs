def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self._keys:
		key = self._keys.pop(0)
		value = self._values.pop(0)
		return (key, value)
	else:
		raise KeyError('popitem(): dictionary is empty')