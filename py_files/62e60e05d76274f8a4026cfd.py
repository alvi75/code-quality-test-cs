def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, str):
		return self._str_index(key)
	elif isinstance(key, int):
		return key
	elif isinstance(key, tuple):
		return self._tuple_index(key)
	else:
		raise TypeError("key must be string or integer")