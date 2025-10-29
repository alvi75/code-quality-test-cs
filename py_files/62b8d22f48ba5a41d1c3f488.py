def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	try:
		key, value = self._items.popitem()
	except KeyError:
		raise KeyError("popitem() on an empty dictionary")
	return key, value