def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if self.__keys is None:
		self.__keys = []
		for k in dir(self):
			if not k.startswith('__'):
				self.__keys.append(k)
	return self.__keys