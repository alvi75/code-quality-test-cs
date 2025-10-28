def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""

	def _deprecated(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			# TODO: add a message to the docstring?
			print("DEPRECATION WARNING: %s is deprecated" % func.__name__)
			return func(*args, **kwargs)

		return wrapper

	return _deprecated