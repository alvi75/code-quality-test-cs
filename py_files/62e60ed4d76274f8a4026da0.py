def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if self.__keys is None:
		self.__keys = []
		for key in dir(self):
			if not key.startswith('_') and hasattr(self, key):
				self.__keys.append(key)
	return self.__keys