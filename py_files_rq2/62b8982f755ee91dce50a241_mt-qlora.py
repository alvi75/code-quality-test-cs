def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	return self.__class__(self._seconds, self._microseconds)