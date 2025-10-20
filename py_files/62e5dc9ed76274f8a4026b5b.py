def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def _deprecated(func):
		@functools.wraps(func)
		def __deprecated(*args, **kwargs):
			warnings.warn(
				"Call to deprecated function {0}.".format(func.__name__),
				category=DeprecationWarning,
				stacklevel=2
			)
			return func(*args, **kwargs)
		return __deprecated
	return _deprecated