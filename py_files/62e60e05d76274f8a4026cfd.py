def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, str):
		key = key.encode('utf-8')
	return self._index(key)