def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	key, value = self.__choice()
	self._remove(key)
	return key, value