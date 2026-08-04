def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if self.__keys is None:
		self.__keys = [k for k in dir(self) if not k.startswith('__')]
	return self.__keys