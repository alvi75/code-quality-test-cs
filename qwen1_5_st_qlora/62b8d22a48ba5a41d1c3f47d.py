def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if self._check_key(key) or (default is __marker and key in self._dict):
		return self._dict.pop(key)
	elif default is __marker:
		raise KeyError(key)
	else:
		return default