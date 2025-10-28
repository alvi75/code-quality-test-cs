def tzname_in_python2(namefunc):
	"""
	Change unicode output into bytestrings in Python 2
	"""
	if sys.version_info[0] == 3:
		return namefunc

	def wrapper(*args, **kwargs):
		result = namefunc(*args, **kwargs)
		if isinstance(result, str):
			return result.encode('ascii')
		else:
			return result

	return wrapper