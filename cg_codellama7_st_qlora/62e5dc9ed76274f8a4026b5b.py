def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			warnings.warn(message, DeprecationWarning, stacklevel=2)
			return func(*args, **kwargs)
		wrapper.__name__ = func.__name__
		wrapper.__doc__ = func.__doc__
		wrapper.__dict__.update(func.__dict__)
		return wrapper
	return decorator