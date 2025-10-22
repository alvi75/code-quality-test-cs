def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def _deprecated(func):
		@functools.wraps(func)
		def new_func(*args, **kwargs):
			warnings.warn(
				"Call to deprecated function/method %s." % func.__name__,
				category=DeprecationWarning,
				stacklevel=2
			)
			return func(*args, **kwargs)
		return new_func
	return _deprecated