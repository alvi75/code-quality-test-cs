def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def _tzname(self, name):
		if isinstance(name, six.text_type):
			return name.encode('utf-8')
		else:
			return name

	return _tzname