def get(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, default is returned.
	"""
	if self._keys.has_key(key):
		return self._values[key]
	else:
		return default