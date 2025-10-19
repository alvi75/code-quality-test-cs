def pop(self, key, default=__marker):
	"""
	D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.
	"""
	if self._size == 0:
		raise KeyError(key)
	if key in self._keys:
		index = self._keys.index(key)
		v = self._values[index]
		self._keys.pop(index)
		self._values.pop(index)
		self._size -= 1
		return v
	elif default != __marker:
		return default
	else:
		raise KeyError(key)