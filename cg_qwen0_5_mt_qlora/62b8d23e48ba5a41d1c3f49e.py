def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	return self.__choice.pop(), self.__choice.choice()