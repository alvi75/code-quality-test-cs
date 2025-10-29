def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not self.__class__.__name__ in dir():
		return []
	names = [self.__class__.__name__]
	for name in dir(self.__class__):
		if name.startswith('_') or name == '__init__':
			continue
		if isinstance(getattr(self.__class__, name), type):
			names.append(name)
		elif hasattr(self, name) and (all or not name.startswith('__')):
			names.append(name)
	return names