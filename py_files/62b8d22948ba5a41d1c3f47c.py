def get(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, default is returned.
	"""
	if key not in self._dict:
		return default
	else:
		return self._dict[key]