def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def _decorator(func):
		def _wrapper(*args, **kwargs):
			print("DEPRECATION WARNING: %s is deprecated" % message)
			return func(*args, **kwargs)
		return _wrapper
	return _decorator