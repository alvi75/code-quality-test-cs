def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
	If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if self._len == 0:
		raise KeyError(key)
	try:
		value = self[key]
	except KeyError:
		if default is __marker:
			raise
		return default
	del self[key]
	self._len -= 1
	return value