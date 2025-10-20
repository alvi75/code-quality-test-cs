def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
	If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if key in self:
		return self._pop(key)
	else:
		if default is __marker:
			raise KeyError(key)
		return default