def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def _tzname_in_python2(self, namefunc):
		if self.tzinfo:
			return namefunc(self.tzinfo)
		else:
			return None

	return _tzname_in_python2