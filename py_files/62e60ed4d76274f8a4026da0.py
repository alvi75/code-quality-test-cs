def keys(self):
	"""
	Returns the __keys property of a class as a List
	"""
	if self.__class__.__dict__.has_key('__keys'):
		return self.__class__.__dict__['__keys']
	else:
		return []