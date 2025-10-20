def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	key = self.__choice()
	value = self[key]
	del self[key]
	return key, value