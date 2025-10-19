def popitem(self):
		"""
		Find, remove and return a random `(key, value)` pair via __choice in the class
		"""
		if self._size == 0:
			return None

		keys = list(self.keys())
		values = list(self.values())

		i = random.randrange(len(keys))
		key = keys[i]
		value = values[i]

		del self[key]
		self._size -= 1

		return key, value