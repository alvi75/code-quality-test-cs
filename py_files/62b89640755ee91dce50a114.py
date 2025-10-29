def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	def wrapper(self, *args, **kwargs):
		result = namefunc(self, *args, **kwargs)
		if PY2:
			return result.encode('utf-8')
		else:
			return result
	return wrapper