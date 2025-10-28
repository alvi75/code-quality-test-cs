def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if not hasattr(self, '__keys'):
		self.__keys = []
		for key in dir(self):
			if key[0] != '_':
				self.__keys.append(key)
		return self.__keys