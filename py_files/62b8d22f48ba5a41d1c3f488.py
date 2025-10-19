def popitem(self):
		"""
		Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
		"""
		if self._size == 0:
			raise KeyError('pop from empty dictionary')
		self._dict.pop(min(self._keys), None)
		return min(self._keys), self._dict[min(self._keys)]