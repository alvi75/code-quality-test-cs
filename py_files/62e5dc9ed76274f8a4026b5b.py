def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			warnings.warn(
				"Call to deprecated function {}. {}".format(func.__name__, message),
				category=DeprecationWarning,
				stacklevel=2,
			)
			return func(*args, **kwargs)
		return wrapper
	return decorator