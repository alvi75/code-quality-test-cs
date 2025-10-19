def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if self._keys is None:
		self.makeKeys()
	if default is __marker:
		return self._data.pop(key)
	else:
		return self._data.pop(key, default)