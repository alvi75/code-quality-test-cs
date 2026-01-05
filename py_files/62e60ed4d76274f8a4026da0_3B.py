def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if not hasattr(self, '__keys'):
		self.__keys = []
	for key in self.__dict__:
		if key.startswith('__key_'):
			self.__keys.append(key[6:])
	return self.__keys