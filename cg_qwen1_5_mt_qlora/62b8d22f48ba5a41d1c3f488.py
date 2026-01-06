def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	key = self._popitem_key()
	value = self[key]
	del self[key]
	return (key, value)