def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if self.__keys is None:
		self.__keys = list(self.__dict__.keys())
	return self.__keys