def popitem(self):
	"""
	Find, remove and return a random `(key, value)` pair via __choice in the class
	"""
	return self.__class__.__choice__(self.items())