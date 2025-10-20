def setdefault(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, the value corresponding to the key is set to default.
	"""
	if key not in self._dict:
		self._dict[key] = default
	return self._dict[key]