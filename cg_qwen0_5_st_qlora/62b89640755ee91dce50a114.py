def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def _tzname_in_python2(self, name):
		if self._tzinfo is None:
			return namefunc(name)
		else:
			return namefunc(self.tzname(name))
	return _tzname_in_python2