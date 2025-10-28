def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def wrapper(self, *args, **kwargs):
		if self._tzinfo is None:
			return namefunc(self, *args, **kwargs)
		return self._tzinfo.tzname(*args, **kwargs)

	return wrapper