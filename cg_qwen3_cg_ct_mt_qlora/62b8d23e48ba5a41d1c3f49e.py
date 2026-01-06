def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.__len__() == 0:
		raise KeyError('popitem(): dictionary is empty')
	key = self.__choice()
	value = self[key]
	del self[key]
	return (key, value)