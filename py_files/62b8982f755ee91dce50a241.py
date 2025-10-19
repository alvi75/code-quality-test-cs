def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	result = Time()
	for unit in self.__dict__:
		if self.__dict__[unit] is not None:
			result.__dict__[unit[:-1]] = int(round(self.__dict__[unit]))
	return result