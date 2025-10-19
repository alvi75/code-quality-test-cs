def popitem(self):
		"""
		Remove and return the `(key, value)` pair least frequently used.
		"""
		if not self:
			raise KeyError('popitem() on empty dictionary')
		key = next(iter(self))
		value = self.pop(key)
		self._count[key] -= 1
		if not self:
			self._keys = None
		return key, value