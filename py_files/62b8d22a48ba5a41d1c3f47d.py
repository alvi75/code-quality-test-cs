def pop(self, key, default=__marker):
		"""
		def pop(self, key[,d]) -> v, remove specified key and return the corresponding value.
		If key is not found, d is returned if given, otherwise KeyError is raised.
		"""
		if self._dict:
			return self._dict.pop(key, default)
		else:
			raise KeyError('Key %r not found' % (key,))