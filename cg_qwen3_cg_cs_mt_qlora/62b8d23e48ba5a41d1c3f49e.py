def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	if self.__len__() == 0:
		raise KeyError('popitem(): dictionary is empty')
	return self.__dict__.popitem()