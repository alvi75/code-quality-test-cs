def popitem(self):
		'''
		"Remove and return the (key, value) pair most recently used.
		'''
		if self._len() == 0:
			raise KeyError('pop from empty Counter')
		self._buckets = [k for k in self._buckets if k]
		if len(self._buckets) == 1:
			return None, None
		key = self._buckets.pop()
		value = self._counts[key] - 1
		if value == 0:
			del self._counts[key]
			del self._buckets[key]
		else:
			self._counts[key] = value
		return key, value