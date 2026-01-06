def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if not self._keys:
		raise KeyError("popitem(): dictionary is empty")
	k, v = self._keys.pop(0)
	return k, v