def get(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, default is returned.
	"""
	if self._dict.has_key(key):
		return self._dict[key]
	else:
		return default