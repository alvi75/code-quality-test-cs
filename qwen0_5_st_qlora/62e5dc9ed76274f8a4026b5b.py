def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def wrapper(func):
		@functools.wraps(func)
		def new_func(*args, **kwargs):
			print("DEPRECATION WARNING: %s" % message)
			return func(*args, **kwargs)
		return new_func
	return wrapper