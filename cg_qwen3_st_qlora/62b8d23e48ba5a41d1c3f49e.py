def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	key, value = self.__choice()
	del self[key]
	return key, value