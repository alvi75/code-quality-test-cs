def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if not self.__keys:
		self.__keys = [key for key in dir(self.__class__) if not key.startswith('__') and not callable(key)]
	return self.__keys