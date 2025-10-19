def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, str):
		key = self._decode_key(key)
	return key if not isinstance(key, int) else None