def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if sys.version_info[0] == 3:
		return namefunc

	def _tzname_in_python2(self, *args, **kwargs):
		return namefunc(*args, **kwargs).encode('ascii')

	tzname.__get__(None).__get__ = _tzname_in_python2
	return tzname