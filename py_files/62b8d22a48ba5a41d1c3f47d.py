def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if key in self._dict:
		return self._dict.pop(key)
	else:
		if default is __marker:
			raise KeyError('Key %s not found' % key)
		elif isinstance(default, collections.Mapping):
			return default
		else:
			raise TypeError('default must be a mapping')