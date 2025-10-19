def popitem(self):
		"""
		Remove and return the `(key, value)` pair least recently used.
		"""
		if not self:
			raise KeyError('popitem() on empty dictionary')
		key = self._keys[0]
		del self[key]
		return key, self[key]