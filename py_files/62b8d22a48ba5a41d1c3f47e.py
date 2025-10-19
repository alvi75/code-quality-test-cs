def setdefault(self, key, default=None):
	"""
	If a key exists in the class, the value corresponding to the key is returned. Otherwise, the value corresponding to the key is set to default.
	"""
	if self.__dict__.has_key(key):
		return self.__dict__[key]
	else:
		self[key] = default
		return default