def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.__size == 0:
		raise KeyError('popitem(): empty dictionary')
	key, value = self.__choice()
	del self[key]
	return key, value