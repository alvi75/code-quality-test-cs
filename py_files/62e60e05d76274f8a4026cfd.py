def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, int):
		return key
	elif isinstance(key, str):
		key = self._key_to_int(key)
		return key
	else:
		raise TypeError("Key must be a string or integer.")