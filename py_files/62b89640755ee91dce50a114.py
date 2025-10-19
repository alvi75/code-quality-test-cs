def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if not isinstance(namefunc, (str, bytes)):
		return namefunc

	if PY3:
		return namefunc.encode('utf-8')

	return namefunc