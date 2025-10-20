def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, str):
		return self._index(key)
	elif isinstance(key, int):
		return key
	else:
		raise TypeError("Key must be a string or integer")